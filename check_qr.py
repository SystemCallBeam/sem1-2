import os
import cv2
from pyzbar import pyzbar

def decode_qrcode(image_path):
    if not os.path.exists(image_path):
        return None, f"File not found: {image_path}"
    
    image = cv2.imread(image_path)
    
    if image is None:
        return None, f"Unable to read image: {image_path}"
    
    qrcodes = pyzbar.decode(image)
    
    if not qrcodes:
        return None, "No QR code found"
    
    qr_data = [qr.data.decode('utf-8') for qr in qrcodes]
    return qr_data, None

image_folder = "C:\\Users\\tkhae\\Desktop\\New folder\\QR"

results = {}
for i in range(1, 100):
    filename = f"{i:02}.jpg"
    image_path = os.path.join(image_folder, filename)  # Create the full path to the image
    
    decoded_data, error = decode_qrcode(image_path)
    
    if error:
        results[filename] = error
    else:
        results[filename] = decoded_data

for filename, response in results.items():
    print(f"{filename}: {response}")