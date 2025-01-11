from PIL import Image
import os

input_folder = "path_to_input_folder"
output_folder = "path_to_output_folder"
target_size_kb = 250  # Target size in KB

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        filepath = os.path.join(input_folder, filename)
        img = Image.open(filepath)
        quality = 85  # Start with high quality
        while True:
            output_path = os.path.join(output_folder, filename)
            img.save(output_path, "JPEG", quality=quality)
            if os.path.getsize(output_path) / 1024 <= target_size_kb:
                break
            quality -= 5  # Gradually reduce quality
