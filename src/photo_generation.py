import os
from PIL import Image
import numpy as np
from imgaug import augmenters as iaa
import imageio
import re

# Cấu hình
dataset_dir = "F:\\DAKHMT\\PKHMT\\dataset"
num_augmented_per_image = 5  # Số ảnh muốn tạo thêm cho mỗi ảnh gốc
image_size = 28

# Hàm augmentation
augmenter = iaa.Sequential([
    iaa.Affine(
        rotate=(-10, 10),
        scale=(0.9, 1.1),
        translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},
    ),
    iaa.LinearContrast((0.8, 1.2)),
])

# Hàm lấy số thứ tự cuối cùng trong tên file
def get_max_index(files, prefix):
    indices = []
    pattern = re.compile(rf"{re.escape(prefix)}_(\d+)\.png")
    for f in files:
        match = pattern.match(f)
        if match:
            indices.append(int(match.group(1)))
    return max(indices) if indices else 0

# Lặp qua từng thư mục ký tự
for char_folder in os.listdir(dataset_dir):
    char_path = os.path.join(dataset_dir, char_folder)
    if not os.path.isdir(char_path):
        continue

    image_files = sorted([f for f in os.listdir(char_path) if f.endswith(".png")])
    print(f"📁 Đang xử lý ký tự: {char_folder} ({len(image_files)} ảnh)")

    max_index = get_max_index(image_files, char_folder)

    for image_file in image_files:
        image_path = os.path.join(char_path, image_file)
        image = Image.open(image_path).convert("L").resize((image_size, image_size))
        image_np = np.array(image)

        for i in range(num_augmented_per_image):
            augmented_image = augmenter(image=image_np)
            max_index += 1
            new_filename = f"{char_folder}_{max_index:03d}.png"
            new_path = os.path.join(char_path, new_filename)
            imageio.imwrite(new_path, augmented_image)

print("✅ Đã sinh thêm ảnh xong theo thứ tự liên tiếp!")
