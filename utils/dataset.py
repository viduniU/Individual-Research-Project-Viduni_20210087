import os
import cv2
import torch
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image, ImageOps

def resize_and_pad(img, size=(128, 32)):
    img = img.convert("L")
    w, h = img.size
    scale = size[1] / h
    new_w = int(w * scale)
    img = img.resize((new_w, size[1]), Image.BILINEAR)

    if new_w > size[0]:
        img = img.resize(size, Image.BILINEAR)
    else:
        delta_w = size[0] - new_w
        padding = (delta_w // 2, 0, delta_w - delta_w // 2, 0)
        img = ImageOps.expand(img, padding, fill=255)

    return img

class HandwritingDataset(Dataset):
    def __init__(self, label_file, img_root, img_size=(128, 32)):
        self.img_root = img_root
        self.img_size = img_size
        self.transform = transforms.Compose([
            transforms.Lambda(lambda img: resize_and_pad(Image.fromarray(img), size=img_size)),
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])

        # Load (filename, label) pairs
        self.data = []
        with open(label_file, 'r') as f:
            for line in f:
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    filename, label = parts
                    self.data.append((filename, label))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        filename, label = self.data[idx]
        img_path = os.path.join(self.img_root, filename)  # FLAT folder logic

        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise ValueError(f"Image not found: {img_path}")
        image = self.transform(image)

        return image, label
