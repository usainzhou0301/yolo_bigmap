import os

def rename_images(folder_path):
    # 获取文件夹中所有图片文件（只考虑jpg、png等图片）
    image_extensions = ['.jpg', '.jpeg', '.png']
    images = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in image_extensions]

    # 按名字排序，确保重命名顺序一致
    images.sort()

    # 避免重名，先把所有图片改成临时名
    for idx, filename in enumerate(images):
        ext = os.path.splitext(filename)[1].lower()
        temp_name = f"temp_{idx}{ext}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, temp_name))

    # 然后再从 0.jpg 开始重命名
    temp_images = [f for f in os.listdir(folder_path) if f.startswith("temp_")]
    temp_images.sort()

    for idx, filename in enumerate(temp_images):
        ext = os.path.splitext(filename)[1].lower()
        new_name = f"{idx}{ext}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

    print(f"重命名完成，共处理 {len(temp_images)} 张图片。")

# 使用方式：把下面路径换成你图片文件夹的路径
rename_images("sample")
