import torch
from torchvision import transforms
from PIL import Image
import numpy as np

# Load the trained model
model = torch.load('model.pth')
model.eval()

# Define the transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def predict(file):
    """
    Predict the occupancy of a parking lot from an image file
    """
    # Open the image file
    img = Image.open(file)
    
    # Apply the transformation and add an extra dimension
    img_t = transform(img)
    img_u = torch.unsqueeze(img_t, 0)
    
    # Perform the prediction
    with torch.no_grad():
        out = model(img_u)
    
    # Convert the output probabilities to occupancy percentage
    
    return torch.nn.functional.softmax(out, dim=1).numpy()[0][1] * 100
    