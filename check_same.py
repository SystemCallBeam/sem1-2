from PIL import Image
import imagehash # type: ignore
import os

folder_path = "C:\\Users\\tkhae\\Desktop\\New folder\\QR"
hashes = {}

# Loop through all images in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Check for image extensions
        img_path = os.path.join(folder_path, filename)
        image = Image.open(img_path)
        hash_value = imagehash.phash(image)  # Compute perceptual hash
        print(f"Image: {filename}, Hash: {hash_value}")

        if hash_value in hashes:
            print(f"{filename} is the same as {hashes[hash_value]}")
        else:
            hashes[hash_value] = filename
