from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load pre-trained BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Get image path
image_path = input("Enter image path: ")

# Open image
image = Image.open(image_path).convert("RGB")

# Process image
inputs = processor(images=image, return_tensors="pt")

# Generate caption
output = model.generate(**inputs)

# Decode caption
caption = processor.decode(output[0], skip_special_tokens=True)

print("\n===== IMAGE CAPTION =====")
print("Caption:", caption)