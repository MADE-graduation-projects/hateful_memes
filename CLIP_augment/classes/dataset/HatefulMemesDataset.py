import torch
import json
import os
from PIL import Image
import cv2
from cv2 import cv2


class HatefulMemesDataset(torch.utils.data.Dataset):
    def __init__(self, data_path, transforms):
        self.data = [json.loads(l) for l in open(data_path)]
        self.data_dir = os.path.dirname(data_path)
        self.transforms = transforms
            
    def __getitem__(self, index: int):
        #image = Image.open(os.path.join(self.data_dir, self.data[index]["img"]))   
        
        path = os.path.join(self.data_dir, self.data[index]["img"])
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        text = self.data[index]["text"]
        label = self.data[index]["label"]

        if self.transforms is not None:
            image = self.transforms(image)
            
        return image, text, label, path
    
    def __len__(self):
        return len(self.data)