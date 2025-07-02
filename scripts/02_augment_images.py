import os
from PIL import Image
from torchvision import transforms

INPUT_DIR = "data/croppeds_hannover/green"
OUTPUT_DIR = "data/croppeds_hannover/green_augmented"
AUGMENT_COEFFICIENT = 6

class CustomAugmentation:
    def __init__(self):
        self.base_transform = transforms.Compose([
            transforms.RandomRotation(degrees=5),
            transforms.RandomHorizontalFlip(p=0.3)
        ])

    def __call__(self, image):
        return self.base_transform(image)

def augment_dataset(input_dir, output_dir, coeff):
    os.makedirs(output_dir, exist_ok=True)
    augmenter = CustomAugmentation()

    image_paths = [f for f in os.listdir(input_dir) if f.lower().endswith('.jpg')]
    print(f"[INFO] Found {len(image_paths)} images.")

    for image_name in image_paths:
        image_path = os.path.join(input_dir, image_name)
        try:
            original_img = Image.open(image_path).convert("RGB")
        except Exception as e:
            print(f"[ERROR] Could not open {image_name}: {e}")
            continue

        base_name = os.path.splitext(image_name)[0]
        original_img.save(os.path.join(output_dir, f"{base_name}_orig.jpg"))

        for i in range(coeff - 1):
            aug_img = augmenter(original_img)
            aug_img.save(os.path.join(output_dir, f"{base_name}_aug{i+1}.jpg"))

    print(f"[DONE] Augmented images saved to {output_dir}")

if __name__ == "__main__":
    augment_dataset(INPUT_DIR, OUTPUT_DIR, AUGMENT_COEFFICIENT)

