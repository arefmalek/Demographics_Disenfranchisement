#goal is to load an image
import torch
import torchvision
import os
import numpy as np
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision.transforms as transforms
from torchvision.transforms import ToTensor
import cv2

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 94 * 94, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84,4)  #age (0 to 1 * 100), gender (<0.5 -> F, >=0.5 -> M), race ((0 to 1) / nraces) 

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 94 * 94)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def process(filename):
    age, race, gender = Net(), Net(), Net()
    
    age.load_state_dict(torch.load("pth_files/age_mse.pth"))
    race.load_state_dict(torch.load("pth_files/race_mse.pth"))
    gender.load_state_dict(torch.load("pth_files/mse_gender.pth"))


    #quick read of myself

    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (200,200))

    tensor_image = torch.from_numpy(img)
    x = torch.reshape(tensor_image, (-1, ))
    torch.reshape(x, (-1,3,200,200))

    y = x.repeat(4,1)
    ti = torch.reshape(y, (4, 3, 200, 200)).float()

    return age(ti), race(ti), gender(ti)
    return age(ti).mean().item(), race(ti).mean().item(), gender(ti).mean().item()

age, race, gender = process("image.jpg")
print(age)
print(race)
print(gender)