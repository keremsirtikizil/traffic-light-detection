import os
import json
import cv2
import numpy as np
from tqdm import tqdm

LABEL_JSON_PATH = "data/jsons/Hannover.json"
IMAGE_BASE_PATH = "data/raw_images"
OUTPUT_CROP_DIR = "data/croppeds_hannover"

STATE_MAP = {
    "red": "red",
    "green": "green",
    "yellow": "yellow",
    "off": "unknown",
    "unknown": "unknown",
    "red_yellow": "yellow"
}

class_counters = {
    "red": 1,
    "green": 1,
    "yellow": 1,
    "unknown": 1
}

def ensure_output_dirs():
    for cls in STATE_MAP.values():
        os.makedirs(os.path.join(OUTPUT_CROP_DIR, cls), exist_ok=True)

def read_driveu_tiff(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img is None:
        return None
    img = cv2.cvtColor(img, cv2.COLOR_BAYER_GB2BGR)
    img = np.right_shift(img, 4)
    return img.astype(np.uint8)

def process_json(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)

    for img_entry in tqdm(data["images"], desc="Cropping lights"):
        rel_path = img_entry["image_path"]
        full_path = os.path.join(IMAGE_BASE_PATH, rel_path)

        if not os.path.exists(full_path):
            print(f"[!] Missing image: {full_path}")
            continue

        image = read_driveu_tiff(full_path)
        if image is None:
            print(f"[!] Could not read: {full_path}")
            continue

        skip_next = False

        for label in img_entry.get("labels", []):
            if skip_next:
                skip_next = False
                continue
            skip_next = True

            attr = label.get("attributes", {})
            raw_state = attr.get("state", "unknown")
            state = STATE_MAP.get(raw_state, "unknown")

            if attr.get("relevance") != "relevant":
                continue

            x, y, w, h = map(int, [label["x"], label["y"], label["w"], label["h"]])

            if w < 5 or h < 5 or abs(w - h) < 10 or h <= w:
                continue

            cropped = image[y:y + h, x:x + w]
            if cropped.size == 0:
                continue

            count = class_counters[state]
            out_path = os.path.join(OUTPUT_CROP_DIR, state, f"{state}{count}.jpg")
            cv2.imwrite(out_path, cropped)
            class_counters[state] += 1

def main():
    ensure_output_dirs()
    process_json(LABEL_JSON_PATH)
    print("Done. Crops saved to:", OUTPUT_CROP_DIR)

if __name__ == "__main__":
    main()

