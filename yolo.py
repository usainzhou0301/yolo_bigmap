from ultralytics import YOLO

# ① 加载预训练模型（可选：yolov8n.pt / yolov8s.pt / yolov8m.pt 等）
model = YOLO("yolov8n.pt")
#
# ② 开始训练
# model.train(
#     data="data.yaml",       # 数据集配置文件路径（需确认图片路径写对）
#     epochs=100,              # 训练轮数
#     batch=32,               # 每批图像数量
#     imgsz=640,              # 图像尺寸
#     device='mps',           # mac 上推荐 mps，如果是 NVIDIA 显卡用 'cuda'
#     project='yolo_project', # 项目保存路径
#     name='v8_run8',         # 子目录名称
#     save=True,              # 是否保存模型
#     verbose=True            # 显示详细日志
# )

# ③ 模型验证（评估 mAP 等指标）
metrics = model.val(data="data.yaml", imgsz=640)

# ④ 打印验证结果（precision/recall/mAP 等）
print("mAP50:", metrics.box.map50)
print("mAP50-95:", metrics.box.map)

# ⑤ 载入训练好的模型
model = YOLO("yolo_project/v8_run8/weights/best.pt")

# ⑥ 对 test/images 中的所有图片进行推理
results = model.predict(source="test/images", save=True, save_txt=True)

# ⑦ 输出预测框信息（每张图）
for i, r in enumerate(results):
    print(f"\n📸 图像 {i + 1}:")
    boxes = r.boxes  # 检测框信息

    if boxes is not None and boxes.xywh is not None:
        for j in range(len(boxes.xywh)):
            cls_id = int(boxes.cls[j].item())
            conf = float(boxes.conf[j].item())
            x, y, w, h = boxes.xywh[j]
            print(f" - 类别: {cls_id}, 置信度: {conf:.2f}, xywh: ({x:.1f}, {y:.1f}, {w:.1f}, {h:.1f})")
        # r.show()  # 使用 show() 显示图像与检测框
    else:
        print(" - 没有检测到目标。")
