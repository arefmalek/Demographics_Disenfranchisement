#goal is to load an image
import torch
import os
import numpy as np
# import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from torchvision.transforms import ToTensor

import cv2
import base64

# THIS IS GONNA BE SUPER USEFUL ONCE WE NEED B64
# from io import BytesIO
# from PIL import Image
# 
# 
# im_bytes = base64.b64decode(im_b64)   # im_bytes is a binary image
# im_file = BytesIO(im_bytes)  # convert image to file-like object

from model import *

age, race, gender = Age(), Race(), Sex()
    
age.load_state_dict(torch.load("pth_files/age.pth"))
race.load_state_dict(torch.load("pth_files/race.pth"))
gender.load_state_dict(torch.load("pth_files/gender.pth"))

    

def process(frame, age = age, race = race, gender = gender):
    img = cv2.resize(frame, (200, 200))
    tensor_image = transforms.ToTensor()(img)
    
    ti = torch.reshape(tensor_image, (1, 3, 200, 200)).float()
    
    product = {
        "Age: ": torch.max(age(ti), 1)[1], 
        "Race: ": torch.max(race(ti), 1)[1], 
        "Gender: ":torch.max(gender(ti), 1)[1]
    }

    return product

def __main__():
    cap = cv2.VideoCapture(0)
    
    while(True):
        ret, frame = cap.read()
    
        cv2.imshow("image", frame)
        print(process(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

print(process(cv2.imread("test_images/arf.jpg")))
