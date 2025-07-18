# yolo_bigmap and weed_detection

The project provides a tool to generate synthetic farmland datasets for weed detection.

The farmland pictures are concatenated using weed samples from the **Weed Image Detection Dataset** [https://www.kaggle.com/datasets/jaidalmotra/weed-detection].
It comprises a diverse range of images featuring different types of weeds commonly found in agricultural and natural environments. These images are annotated to provide valuable information for training and evaluating computer vision models and algorithms.

An examplary farmland picture is presented as follows:
<img width="1280" height="1280" alt="image" src="https://github.com/user-attachments/assets/5d1f617c-5ecf-45eb-bb3f-fe5c08d14cb3" />


In addition, **YOLOv8** [https://yolov8.com/] is used for weed detection for each farmland pictures. The type of grass is trained from the annotated pitures in the Weed Image Detection Dataset.
An examplary weed detection result is presented as follows:
<img width="640" height="640" alt="image" src="https://github.com/user-attachments/assets/fe7ab6e4-2d99-47f9-be3e-a96b289a5f0b" />
