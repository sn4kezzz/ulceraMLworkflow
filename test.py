import torch
from torchvision import datasets, transforms
from Models import fcbformer
import torchvision
from PIL import Image
model = fcbformer.FCBFormer()

print(torch.cuda.device_count())
