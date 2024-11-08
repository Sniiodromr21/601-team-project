import os
import ants

# Define the directory containing the .nii.gz images
input_dir = r'E:/Boston_University/nii_gz/Unprocessed/mpr_n4_anon_111_t88_masked_gfc_tra_90_nii_gz'
output_dir = r'E:/Boston_University/nii_gz/Processed/mpr_n4_anon_111_t88_masked_gfc_tra_90_segmented'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop through all .nii.gz files in the input directory
for nii_path in os.listdir(input_dir):
    if nii_path.endswith('.nii.gz'):
        # Load the NIfTI image
        img_path = os.path.join(input_dir, nii_path)
        img = ants.image_read(img_path)
        
        # Check image dimensions (ensure it's 3D)
        if img.dimension != 3:
            print(f"Skipping {nii_path} as it is not a 3D image.")
            continue
        
        # Preprocess the image (bias field correction)
        img_corrected = ants.n4_bias_field_correction(img)

        # Normalize the image to improve segmentation results
        img_corrected = ants.iMath_normalize(img_corrected)

        # Generate a brain mask
        brain_mask = ants.get_mask(img_corrected)

        # Attempt segmentation with a simple model
        try:
            segmentation = ants.atropos(
                a=img_corrected,
                x=brain_mask,
                i='kmeans[3]',
                m='[0.2,1x1x1]',  # Set mrf (Markov random field) parameter explicitly
                c='[5,0]',  # Convergence: max 5 iterations, no smoothing
                priorweight=0.5,  # Set prior weight (reduces reliance on priors if any)
                verbose=1
            )

            # Save the segmented output
            base_name = nii_path.replace('.nii.gz', '_segmented.nii.gz')
            output_path = os.path.join(output_dir, base_name)
            ants.image_write(segmentation['segmentation'], output_path)

            #print(f"Processed and segmented {nii_path}, saved as {output_path}")

        except Exception as e:
            print(f"Failed to segment {nii_path}. Error: {e}")

print("Processing completed.")