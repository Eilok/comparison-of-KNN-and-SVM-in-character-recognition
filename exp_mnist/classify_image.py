import os
import shutil

# Define the source folder containing images and the base target folder
source_folder = "experiment\exp_mnist\DataImages-Test"  # Modify with the actual path to the image folder
target_folder_base = "/data/test"  # Modify with the actual base path to the target folder

# Traverse files in the source image folder
for filename in os.listdir(source_folder):
    if filename.endswith(".png"):  # Assume images are in JPG format
        # Parse the last digit from the filename
        last_digit = int(filename.split("-")[-1].split(".")[0])

        # Create the target folder path
        target_folder = os.path.join(target_folder_base, str(last_digit))

        # If the target folder does not exist, create it
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # Build the source and target file paths
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_folder, filename)

        # Move the file to the target folder
        shutil.move(source_path, target_path)

print("Classification completed.")
