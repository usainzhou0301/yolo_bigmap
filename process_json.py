import os
import json

def convert_coco_to_yolo(json_path, images_dir, labels_dir):
    with open(json_path, 'r') as f:
        coco = json.load(f)

    os.makedirs(labels_dir, exist_ok=True)

    # 映射 image_id → file_name
    image_id_to_name = {img['id']: img['file_name'] for img in coco['images']}
    image_id_to_size = {img['id']: (img['width'], img['height']) for img in coco['images']}
    annotations = coco['annotations']

    # 映射 image_id → [ann1, ann2, ...]
    image_to_anns = {}
    for ann in annotations:
        image_to_anns.setdefault(ann['image_id'], []).append(ann)

    all_image_ids = set(image_id_to_name.keys())
    created = 0

    for image_id in all_image_ids:
        file_name = image_id_to_name[image_id]
        width, height = image_id_to_size[image_id]
        txt_name = os.path.splitext(file_name)[0] + '.txt'
        txt_path = os.path.join(labels_dir, txt_name)

        lines = []
        for ann in image_to_anns.get(image_id, []):
            cat_id = ann['category_id']  # 这里直接用原始的类别ID（YOLO支持）
            bbox = ann['bbox']
            x, y, w, h = bbox
            xc = (x + w / 2) / width
            yc = (y + h / 2) / height
            wn = w / width
            hn = h / height
            lines.append(f"{cat_id} {xc:.6f} {yc:.6f} {wn:.6f} {hn:.6f}")

        with open(txt_path, 'w') as f:
            f.write('\n'.join(lines))
        created += 1

    print(f"✅ 共生成 {created} 个 .txt 标签文件，保存在 {labels_dir}")

# 使用
convert_coco_to_yolo(
    json_path='test/_annotations.coco.json',
    images_dir='test/images',  # 目前只用来对齐图片名，其实不是必须
    labels_dir='test/labels'  # 自动创建
)
