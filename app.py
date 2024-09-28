import torch
from PIL import Image, ImageDraw, ImageFont
from transformers import ViTForImageClassification, ViTImageProcessor
import sys

# Load the model and processor
model = ViTForImageClassification.from_pretrained("google/vit-base-patch16-224")
processor = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")

# Load class labels from the model's configuration
class_labels = model.config.id2label

def classify_image(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_idx = logits.argmax(-1).item()
    predicted_class_name = class_labels[predicted_class_idx]  # Get the class name
    return predicted_class_idx, predicted_class_name, image

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    class_idx, class_name, image = classify_image(image_path)
    
    # Print the results
    print(f"Predicted class index: {class_idx}")
    print(f"Predicted class name: {class_name}")

    # Display the image with the class name
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # Load default font
    text_position = (10, 10)  # Position for the text
    draw.text(text_position, f"Predicted: {class_name}", fill="red", font=font)

    # Show the image
    image.show()
