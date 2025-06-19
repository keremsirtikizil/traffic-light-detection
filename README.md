# traffic-light-detection

# 🚦 Traffic Light Detection and Classification with YOLO and DriveU Dataset

This project explores camera-based **traffic light detection and classification** using **deep neural networks (DNNs)**. The goal is to **replace the legacy MobileNetV2 classifier** with a more powerful, modern architecture (e.g., YOLOv8 or YOLO-NAS), fine-tuned on the **DriveU Traffic Light Dataset (DTLD)** for robust, real-world performance in autonomous driving systems.

---

## 📌 Project Overview

- **Object Detection**: Performed using [YOLOv11](https://docs.ultralytics.com/models/yolo11/) trained on the [COCO dataset](https://cocodataset.org/#home).
- **Traffic Light Classification**: Originally handled by **MobileNetV2**, fine-tuned on a Japanese dataset.
- **Planned Upgrade**: Replace MobileNetV2 with a more accurate model, trained and tested on the **DriveU Traffic Light Dataset (DTLD)**.

---

## 📂 Repository Structure

```bash
├── dtld_parsing/             # Clone of DTLD parsing tools
│   └── python/               # Scripts to extract crops and parse labels
├── data/
│   ├── DTLD/                 # Contains stereo images and city folders
│   └── DTLD_labels_v2.0/     # JSON-formatted annotations
├── webcam_test/              # YOLO webcam test scripts
├── yolo_models/              # Wrapper to test different YOLO models
├── utils/                    # Helper functions for parsing, visualization
└── README.md
