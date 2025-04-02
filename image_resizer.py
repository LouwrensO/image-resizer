import os
from PIL import Image

# 🔧 Set your folder path here
source_folder = "C:/Users/user/Desktop/test_images"
output_folder = "C:/Users/user/Desktop/resized_images"

# Resize scale (e.g., 0.5 = 50% size)
scale = 0.5

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through images in the folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(source_folder, filename)
        img = Image.open(image_path)

        # Resize
        new_size = (int(img.width * scale), int(img.height * scale))
        resized_img = img.resize(new_size)

        # Save resized image
        save_path = os.path.join(output_folder, filename)
        resized_img.save(save_path)

        print(f"✅ Resized: {filename} → {new_size}")

print("🎉 All images resized!")
