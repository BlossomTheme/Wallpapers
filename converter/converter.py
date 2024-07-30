from PIL import Image
import numpy as np
import os

def convert_to_two_color(input_path, output_path, color1, color2, threshold=128):
    img = Image.open(input_path).convert('L')  # Convert to grayscale

    img_array = np.array(img)

    mask = img_array > threshold

    result = np.zeros((*img_array.shape, 3), dtype=np.uint8)

    result[mask] = color1
    result[~mask] = color2

    result_img = Image.fromarray(result)

    result_img.save(output_path)

input_folder = "input"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

color1 = (255, 5, 141) 
color2 = (16, 17, 27)

for filename in os.listdir(input_folder):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"two_color_{filename}")
        convert_to_two_color(input_path, output_path, color1, color2)

print("Conversion complete!")