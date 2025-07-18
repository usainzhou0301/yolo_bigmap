# yolo_bigmap

The project provides a tool to generate synthetic farmland datasets for weed detection.

The farmland pictures are concatenated using weed samples from the **Weed Image Detection Dataset**[https://www.kaggle.com/datasets/jaidalmotra/weed-detection].
It comprises a diverse range of images featuring different types of weeds commonly found in agricultural and natural environments. These images are annotated to provide valuable information for training and evaluating computer vision models and algorithms.

In addition, **YOLOv8**[https://yolov8.com/] is used for weed detection for each farmland pictures. The type of grass is trained from the annotated pitures in the Weed Image Detection Dataset.
