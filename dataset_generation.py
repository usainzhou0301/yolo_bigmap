import os
import random
import numpy as np
from PIL import Image, ImageFilter

def create_collage_with_labels(
    image_folder,
    output_image_path,
    output_label_path,
    grid_size=40,
    base_num=1600,
    replace_count=60,
    swap_ratio=0.05,
    target_cell_size=(32, 32)  # 显示时压缩每张小图
):
    total_cells = grid_size * grid_size
    labels = list(range(total_cells))

    # 1. 替换60个编号为1600-1662
    replace_indices = random.sample(range(total_cells), replace_count)
    replacement_values = random.sample(range(base_num, base_num + replace_count), replace_count)
    for idx, val in zip(replace_indices, replacement_values):
        labels[idx] = val

    # 2. 交换5%位置
    swap_count = int(total_cells * swap_ratio)
    for _ in range(swap_count):
        i, j = random.sample(range(total_cells), 2)
        labels[i], labels[j] = labels[j], labels[i]

    # 3. 创建编号矩阵
    label_matrix = np.array(labels).reshape((grid_size, grid_size))

    # 4. 读取并压缩小图
    images = []
    for label in labels:
        img_path = os.path.join(image_folder, f"{label}.jpg")
        img = Image.open(img_path).convert("RGB")
        img = img.resize(target_cell_size)  # ⚠️ 只在拼图中压缩，不改原图
        images.append(img)

    # 5. 拼接大图
    cell_w, cell_h = target_cell_size
    collage = Image.new('RGB', (cell_w * grid_size, cell_h * grid_size))
    for i in range(grid_size):
        for j in range(grid_size):
            idx = i * grid_size + j
            collage.paste(images[idx], (j * cell_w, i * cell_h))

    # 6. 模糊缝隙处理
    blurred = collage.filter(ImageFilter.GaussianBlur(radius=1))
    collage = Image.blend(collage, blurred, alpha=0.2)

    # 7. 保存拼图图像和标签矩阵
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    collage.save(output_image_path)

    os.makedirs(os.path.dirname(output_label_path), exist_ok=True)
    np.save(output_label_path, label_matrix)

    print(f"✅ 已保存: {output_image_path} 和标签 {output_label_path}")

def generate_dataset(
    image_folder,
    count=100,
    dataset_dir="dataset",
    label_dir="label",
    target_cell_size=(32, 32)
):
    for i in range(1, count + 1):
        output_image = os.path.join(dataset_dir, f"{i}.png")
        output_label = os.path.join(label_dir, f"{i}.npy")
        create_collage_with_labels(
            image_folder=image_folder,
            output_image_path=output_image,
            output_label_path=output_label,
            target_cell_size=target_cell_size
        )
        print(f"[{i}/{count}] ✅ 完成")

# 🚀 修改这个路径为你的小图文件夹路径（包含 0.jpg ~ 1662.jpg）
image_folder = "sample"

# ⚙️ 开始生成100张拼图（你可以改为50、200等）
generate_dataset(image_folder=image_folder, count=10, target_cell_size=(32, 32))
