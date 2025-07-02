import os
import shutil
from pathlib import Path
from tqdm import tqdm

crop_folders = [
    "data/croppeds_berlin",
    "data/croppeds_bochum",
    "data/croppeds_bremen",
    "data/croppeds_dortmund",
    "data/croppeds_duesseldorf",
    "data/croppeds_essen",
    "data/croppeds_frankfurt",
    "data/croppeds_fulda",
    "data/croppeds_hannover",
    "data/croppeds_koeln"
]

output_root = Path("data/whole_dataset")
classes = ["red", "green", "yellow", "unknown"]

for cls in classes:
    os.makedirs(output_root / cls, exist_ok=True)

counters = {cls: 1 for cls in classes}

for cls in classes:
    for folder in crop_folders:
        src_dir = Path(folder) / cls
        if not src_dir.exists():
            print(f"[!] Missing folder: {src_dir}")
            continue

        for img_path in tqdm(src_dir.glob("*.jpg"), desc=f"{cls} from {src_dir.name}", leave=False):
            new_name = f"{cls}_{counters[cls]}.jpg"
            dst_path = output_root / cls / new_name
            shutil.copy(img_path, dst_path)
            counters[cls] += 1

print("All images copied to whole_dataset/")

