import os
import nibabel as nib
import matplotlib.pyplot as plt

# Define the directory containing the segmented .nii.gz images
nii_dir = r'E:/Boston_University/nii_gz/Processed/mpr_n4_anon_111_t88_gfc_sag_95_segmented'

# Function to display slices from a 3D NIfTI image
def display_nii_slices(nii_path):
    # Load the NIfTI image
    img = nib.load(nii_path)
    data = img.get_fdata()

    # Display the middle slice in each dimension (axial, coronal, sagittal)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(f"Displaying slices from {os.path.basename(nii_path)}")

    # Axial (top-down view)
    middle_slice_axial = data.shape[2] // 2
    axes[0].imshow(data[:, :, middle_slice_axial], cmap='gray')
    axes[0].set_title('Axial Slice')
    axes[0].axis('off')

    # Coronal (front-to-back view)
    middle_slice_coronal = data.shape[1] // 2
    axes[1].imshow(data[:, middle_slice_coronal, :], cmap='gray')
    axes[1].set_title('Coronal Slice')
    axes[1].axis('off')

    # Sagittal (side view)
    middle_slice_sagittal = data.shape[0] // 2
    axes[2].imshow(data[middle_slice_sagittal, :, :], cmap='gray')
    axes[2].set_title('Sagittal Slice')
    axes[2].axis('off')

    plt.show()

# Loop through all .nii.gz files in the directory and display them
for nii_path in os.listdir(nii_dir):
    if nii_path.endswith('.nii.gz'):
        display_nii_slices(os.path.join(nii_dir, nii_path))