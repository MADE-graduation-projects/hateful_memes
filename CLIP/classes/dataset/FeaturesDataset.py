import torch


class FeaturesDataset(torch.utils.data.Dataset):
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels
            
    def __getitem__(self, index: int):            
        return self.features[index], self.labels[index]
    
    def __len__(self):
        return len(self.features)