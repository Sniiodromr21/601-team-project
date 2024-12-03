import cv2
import numpy as np
import os

# Define paths
input_dir = '/home/wsoxl/601/train_images/'  # Input directory containing images
output_base_dir = '/home/wsoxl/601/playground_train/'  # Base directory for output

# Subdirectories for output
thresholded_dir = os.path.join(output_base_dir, 'thresholded/')
contours_dir = os.path.join(output_base_dir, 'contours/')

# Create directories if they don't exist
os.makedirs(thresholded_dir, exist_ok=True)
os.makedirs(contours_dir, exist_ok=True)

# Process all JPG images in the directory
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg'):  # Check for JPG files
        image_path = os.path.join(input_dir, filename)
        
        # Load the image in color
        image = cv2.imread(image_path)

        # Convert to grayscale
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian Blur to reduce noise
        blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

        # Thresholding for segmentation
        _, thresholded_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Save the thresholded image
        thresholded_path = os.path.join(thresholded_dir, f"{os.path.splitext(filename)[0]}_thresholded.png")
        cv2.imwrite(thresholded_path, thresholded_image)
        print(f"Thresholded image saved as '{thresholded_path}'")

        # Find contours in the thresholded image
        contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Create a copy of the grayscale image to visualize contours
        contour_visualization = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR)
        cv2.drawContours(contour_visualization, contours, -1, (0, 255, 0), 1)  # Draw contours in green

        # Save the contours visualization
        contour_path = os.path.join(contours_dir, f"{os.path.splitext(filename)[0]}_contours.png")
        cv2.imwrite(contour_path, contour_visualization)
        print(f"Contours visualization saved as '{contour_path}'")

print("Processing complete for all images.")