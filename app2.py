# app.py
import torch
from PIL import Image
from transformers import ViTForImageClassification, ViTImageProcessor
import sys

model = ViTForImageClassification.from_pretrained("google/vit-base-patch16-224")
processor = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")
image_path="Images/dog.4124.jpg"
def classify_image(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_idx = logits.argmax(-1).item()
    return predicted_class_idx

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    class_idx = classify_image(image_path)
    print(f"Predicted class index: {class_idx}")
