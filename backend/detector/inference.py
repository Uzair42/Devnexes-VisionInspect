import os
from PIL import Image
from django.conf import settings

try:
    import torch
    import torch.nn as nn
    from torchvision import models, transforms
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    print("Warning: PyTorch is not installed. Inference will not work.")

# Define the classes based on your dataset
CLASSES = ['Bridge_Crack_Image', 'CrackForest', 'DeepPCB', 'Magnetic-Tile-Defect']
NUM_CLASSES = len(CLASSES)

# Path where the downloaded weights should be placed
WEIGHTS_PATH = os.path.join(settings.BASE_DIR, 'model_weights.pth')

if TORCH_AVAILABLE:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
else:
    device = None

def load_model():
    """Load the model architecture and weights."""
    if not TORCH_AVAILABLE:
        return None, False
        
    model = models.mobilenet_v2(pretrained=False)
    model.classifier[1] = nn.Linear(model.last_channel, NUM_CLASSES)
    
    if os.path.exists(WEIGHTS_PATH):
        try:
            model.load_state_dict(torch.load(WEIGHTS_PATH, map_location=device))
            model.eval()
            model.to(device)
            return model, True
        except Exception as e:
            print(f"Error loading weights: {e}")
            return None, False
    else:
        return None, False

# Initialize model globally so it's loaded only once when the server starts
model_instance, weights_loaded = load_model()

def predict_image(image_path):
    """Run inference on a single image."""
    if not TORCH_AVAILABLE:
        return "PyTorch is not installed. Please install 'torch' and 'torchvision'."
        
    if not weights_loaded or model_instance is None:
        return "Model weights not found. Please place 'model_weights.pth' in the backend directory."

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    try:
        image = Image.open(image_path).convert('RGB')
        input_tensor = transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            outputs = model_instance(input_tensor)
            _, predicted = outputs.max(1)
            class_idx = predicted.item()
            
        return f"Prediction: {CLASSES[class_idx]}"
    except Exception as e:
        return f"Error during inference: {str(e)}"
