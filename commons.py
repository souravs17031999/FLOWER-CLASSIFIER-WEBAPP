import io
import PIL
import torch
import torch.nn as nn
from torchvision import models
from PIL import Image
import torchvision.transforms as transforms

def get_model():
	checkpoint_path = 'classifier.pt'
	model = models.resnet152(pretrained=True)
	model.fc = nn.Sequential(nn.Linear(2048, 512),nn.ReLU(),nn.Linear(512,102),nn.LogSoftmax(dim=1))    
	model.load_state_dict(torch.load(checkpoint_path,map_location='cpu'),strict=False)
	model.eval()
	return model

def get_tensor(image_bytes):
	my_transforms = transforms.Compose([transforms.Resize(256),
                                      transforms.CenterCrop(224),
                                      transforms.ToTensor(),
                                      transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])])
	
	image = Image.open(io.BytesIO(image_bytes))
	return my_transforms(image).unsqueeze(0)