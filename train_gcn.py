import os
import cv2
import numpy as np
import torch
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv
import torch.nn.functional as F
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# 1. Paths and Parameters
# -----------------------------

preprocessed_dir = '/home/wsoxl/601/Trial_3/train_images/'  # Thresholded ROI images
#contour_dir = '/home/wsoxl/601/playground_train/contours/'  # Contour ROI images
test_preprocessed_dir = '/home/wsoxl/601/Trial_3/test_images/'  # Test thresholded images
#test_contour_dir = '/home/wsoxl/601/playground_test/contours/'  # Test contour images

# Similarity threshold for edge creation
SIMILARITY_THRESHOLD = 0.7

# -----------------------------
# 2. Helper Functions
# -----------------------------

def load_and_extract_features(image_dir):
    """Load images, extract features, and generate labels."""
    features = []
    filenames = []
    labels = []

    sorted_filenames = sorted(os.listdir(image_dir))
    for filename in sorted_filenames:
        if filename.endswith('.jpg'):  # Process only PNG images
            image_path = os.path.join(image_dir, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            
            # Resize to uniform size
            resized_image = cv2.resize(image, (64, 64))
            
            # Extract features
            mean_intensity = np.mean(resized_image)
            std_intensity = np.std(resized_image)
            max_intensity = np.max(resized_image)
            histogram = cv2.calcHist([resized_image], [0], None, [16], [0, 256]).flatten()
            
            # Combine features
            feature_vector = [mean_intensity, std_intensity, max_intensity] + histogram.tolist()
            features.append(feature_vector)
            filenames.append(filename)
            
            # Extract label from filename
            if 'mild' in filename.lower() and 'moderate' not in filename.lower():
                labels.append(0)  # Mild
            elif 'verymild' in filename.lower():
                labels.append(1)  # Very Mild
            elif 'non' in filename.lower():
                labels.append(2)  # Non
            elif 'moderate' in filename.lower():
                labels.append(3)  # Moderate
            else:
                raise ValueError(f"Unknown label in filename: {filename}")

    return np.array(features), labels, filenames

def create_graph(features, similarity_threshold):
    """Create graph structure based on feature similarity."""
    similarity_matrix = cosine_similarity(features)
    edges = []
    for i in range(len(similarity_matrix)):
        for j in range(len(similarity_matrix)):
            if i != j and similarity_matrix[i][j] > similarity_threshold:
                edges.append([i, j])
    edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()
    return edge_index

# -----------------------------
# 3. Load Training Data
# -----------------------------

# Load features and labels for training
preprocessed_features, preprocessed_labels, _ = load_and_extract_features(preprocessed_dir)
#contour_features, contour_labels, _ = load_and_extract_features(contour_dir)

# Ensure labels match
#assert preprocessed_labels == contour_labels, "Labels mismatch between preprocessed and contour images"

# Combine features from thresholded and contour images
#combined_features = np.concatenate((preprocessed_features, contour_features), axis=1)
labels = preprocessed_labels

# Create graph
#train_edge_index = create_graph(combined_features, SIMILARITY_THRESHOLD)
#node_features = torch.tensor(combined_features, dtype=torch.float)
train_edge_index = create_graph(preprocessed_features, SIMILARITY_THRESHOLD)
node_features = torch.tensor(preprocessed_features, dtype=torch.float)
node_labels = torch.tensor(labels, dtype=torch.long)

# Create graph data object
graph_data = Data(x=node_features, edge_index=train_edge_index, y=node_labels)

# Split data for training and validation
num_nodes = len(node_labels)
train_mask = torch.zeros(num_nodes, dtype=torch.bool)
val_mask = torch.zeros(num_nodes, dtype=torch.bool)
train_mask[:int(0.8 * num_nodes)] = True
val_mask[int(0.8 * num_nodes):] = True
graph_data.train_mask = train_mask
graph_data.val_mask = val_mask

# -----------------------------
# 4. Define GCN Model
# -----------------------------

class GCNModel(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GCNModel, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, output_dim)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return x

# Model parameters
#input_dim = combined_features.shape[1]
input_dim = preprocessed_features.shape[1]
hidden_dim = 64
output_dim = 4  # Mild, Very Mild, Non, Moderate

model = GCNModel(input_dim, hidden_dim, output_dim)

# -----------------------------
# 5. Train the Model
# -----------------------------

optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = torch.nn.CrossEntropyLoss()

def train():
    model.train()
    optimizer.zero_grad()
    out = model(graph_data.x, graph_data.edge_index)
    loss = criterion(out[graph_data.train_mask], graph_data.y[graph_data.train_mask])
    loss.backward()
    optimizer.step()
    return loss.item()

def validate():
    model.eval()
    with torch.no_grad():
        out = model(graph_data.x, graph_data.edge_index)
        val_loss = criterion(out[graph_data.val_mask], graph_data.y[graph_data.val_mask]).item()
        val_pred = out[graph_data.val_mask].argmax(dim=1)
        val_acc = (val_pred == graph_data.y[graph_data.val_mask]).sum().item() / graph_data.val_mask.sum().item()
    return val_loss, val_acc

# Train the model
epochs = 50
for epoch in range(1, epochs + 1):
    train_loss = train()
    val_loss, val_acc = validate()
    print(f"Epoch {epoch}, Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}, Val Accuracy: {val_acc:.4f}")

torch.save(model.state_dict(), 'gcn_model.pth')
print("Model saved as gcn_model.pth")

# -----------------------------
# 6. Test the Model
# -----------------------------

# Load test data
test_preprocessed_features, test_labels, _ = load_and_extract_features(test_preprocessed_dir)
#test_contour_features, _, _ = load_and_extract_features(test_contour_dir)

# Combine test features
#test_combined_features = np.concatenate((test_preprocessed_features, test_contour_features), axis=1)

# Create test graph
test_edge_index = create_graph(test_preprocessed_features, SIMILARITY_THRESHOLD)
#test_edge_index = create_graph(test_combined_features, SIMILARITY_THRESHOLD)
test_node_features = torch.tensor(test_preprocessed_features, dtype=torch.float)
#test_node_features = torch.tensor(test_combined_features, dtype=torch.float)
test_labels = torch.tensor(test_labels, dtype=torch.long)

test_graph_data = Data(x=test_node_features, edge_index=test_edge_index, y=test_labels)

# Test the model
model.eval()
with torch.no_grad():
    output = model(test_graph_data.x, test_graph_data.edge_index)
    predictions = output.argmax(dim=1)
    accuracy = (predictions == test_graph_data.y).sum().item() / len(test_graph_data.y)
    print(f"Test Accuracy: {accuracy * 100:.2f}%")
