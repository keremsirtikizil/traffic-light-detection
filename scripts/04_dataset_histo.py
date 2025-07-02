import os
import cv2
import matplotlib.pyplot as plt
from pathlib import Path

dataset_path = Path("data/whole_dataset")

widths, heights = [], []

for class_dir in dataset_path.iterdir():
    if class_dir.is_dir():
        for img_path in class_dir.glob("*.jpg"):
            img = cv2.imread(str(img_path))
            if img is not None:
                h, w = img.shape[:2]
                heights.append(h)
                widths.append(w)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.hist(widths, bins=50, color='blue', alpha=0.7)
plt.title("Image Width Distribution")
plt.xlabel("Width (pixels)")
plt.ylabel("Count")

plt.subplot(1, 2, 2)
plt.hist(heights, bins=50, color='green', alpha=0.7)
plt.title("Image Height Distribution")
plt.xlabel("Height (pixels)")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

