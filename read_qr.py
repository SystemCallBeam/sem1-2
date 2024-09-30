import os
import cv2
from pyzbar.pyzbar import decode

# Define the path to the directory containing the images
image_directory = "C:\\Users\\tkhae\\Desktop\\New folder\\QR"  # Change this to your image path

# List to hold decoded QR codes
qr_codes = []

# Iterate through each image file in the directory
for filename in os.listdir(image_directory):
    if filename.endswith((".png", ".jpg", ".jpeg")):  # Add other image formats if needed
        filepath = os.path.join(image_directory, filename)
        
        # Read the image
        image = cv2.imread(filepath)
        
        # Decode QR codes
        decoded_objects = decode(image)
        
        # Collect decoded QR code data
        for obj in decoded_objects:
            qr_codes.append({
                'filename': filename,
                'data': obj.data.decode('utf-8')  # Decode bytes to string
            })

# Print all found QR codes and their associated filenames
for code in qr_codes:
    print(f"Filename: {code['filename']}, QR Code Data: {code['data']}")
