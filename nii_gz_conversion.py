import os
import glob
import nibabel as nib
import numpy as np
from PIL import Image

# Define source and destination directories
source_dir = 'E://Boston_University/gif/mpr_n4_anon_111_t88_masked_gfc_tra_90_gif'
destination_dir = 'E://Boston_University/nii_gz/mpr_n4_anon_111_t88_masked_gfc_tra_90_nii_gz'

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Define the file pattern to match GIF files
file_pattern = os.path.join(source_dir, 'OAS1_????_MR1_mpr_n4_anon_111_t88_masked_gfc_tra_90.gif')

# Loop through all matching files
for gif_path in glob.glob(file_pattern):
    # Load the GIF and convert frames to a 3D numpy array
    im = Image.open(gif_path)
    frames = []
    try:
        while True:
            frames.append(np.array(im))
            im.seek(im.tell() + 1)
    except EOFError:
        pass  # End of GIF frames

    # Stack frames into a 3D array
    img_data = np.stack(frames, axis=-1)  # Assuming frames are stacked along the third dimension

    # Create NIfTI image
    affine = np.eye(4)  # Identity matrix as affine; adjust if needed
    nifti_img = nib.Nifti1Image(img_data, affine)

    # Save as .nii.gz in the destination folder
    # Generate the output filename based on the input filename
    base_name = os.path.basename(gif_path).replace('.gif', '.nii.gz')
    output_path = os.path.join(destination_dir, base_name)
    nib.save(nifti_img, output_path)

    print(f"Converted {gif_path} to {output_path}")

print("Conversion completed.")