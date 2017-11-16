# References:
# 1. https://blog.uploadcare.com/the-fastest-production-ready-image-resize-out-there-part-0-7c974d520ad9
# 2. https://github.com/python-pillow/Pillow & https://pillow.readthedocs.io/en/latest/handbook/index.html
# 3. https://github.com/uploadcare/pillow-simd & https://pillow.readthedocs.io/en/latest/handbook/index.html
# 3. https://github.com/pytorch/vision

import pandas as pd
import numpy as np
from PIL import Image

import torch
import torchvision
from torchvision.transforms import *

import os

os.getcwd()+"/../data/dog.jpg"
os.getcwd()

# Reading image using PIL
im = Image.open(os.getcwd()+"/data/dog.jpg")
im

# Check type of the object
type(im)

# To know the dimensions, look at the size
im.size

# Converting PIL image to numpy array
im_numpy = np.array(im)
im_numpy

# Shape of the numpy array
im_numpy.shape

# Note that numpy array follows height x width x channels format.
# To convert this numpy array into a PyTorch tensor, we have to reshape it since
# PyTorch follows a batch (n) x channels x height x width (NCHW) format.
# Hence, while reshaping the last axis comes first, then the width axis, then the height axis.

np.transpose(im_numpy, (2, 0, 1)) # 2nd axis first, then 0th axis, then 1st axis.

# Converting numpy array back to PIL
Image.fromarray(im_numpy)

# Creating PyTorch tensor from ndarray
im_torch = torch.from_numpy(im_numpy)
im_torch.size()



# Reshaping the torch tensor. Numpy's reshape analogous to PyTorch's view
im_torch.view((3, 720, 1280))

print(im_torch.size())

topil = torchvision.transforms.ToPILImage()
topil(im_torch.view((3, 720, 1280)))


# Torchvision is a specific library for PyTorch users that deals with several Image
# manipulation routines for machine learning tasks.
torchvision.get_image_backend()

# In PyTorch, in one go, we could do all the transformations required by mentioning
# all the trafos in a compose block.
torchvision.transforms.Compose([
    transforms.CenterCrop(10),
    transforms.ToTensor()
])


# Resizing
# 1. Define Resizing
# Resizing : Almost always done by convolution-based resampling. This technique preserves the quality
# of the original image. This resampling method takes into account as many nearest neighbor pixels

# 2. Show it with examples
# 3. Explain why resizing often leads to poorer performance (interpolation).
# Full-res gets better results. Explain why?

# Extracting each channel from PIL
r, g, b = im.split()
b

# Transforms
## Rotate
im.rotate(60)

## Crop
box = (50, 50, 200, 200)
region = im.crop(box)
region
