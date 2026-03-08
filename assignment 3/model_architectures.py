import torch
import torch.nn as nn

# --- Model Architectures ---

class MLP_MFCC(nn.Module):
    def __init__(self):
        super().__init__()
        # Input features: 40 (mean) + 40 (std) = 80 per MFCC audio clip
        # Parameters: 80*1024 + 1024*100 + 100*50 = ~189k (safely beneath 200k)
        self.net = nn.Sequential(
            nn.Linear(80, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(1024, 100),
            nn.BatchNorm1d(100),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(100, 50)
        )
        
    def forward(self, x): 
        # x is (Batch, 40, 108)
        x_mean = x.mean(dim=2)
        x_std = x.std(dim=2)
        x_pooled = torch.cat([x_mean, x_std], dim=1) # Shape: (Batch, 80)
        return self.net(x_pooled)

class MLP_Mel(nn.Module):
    def __init__(self):
        super().__init__()
        # Input features: 128 (mean) + 128 (std) = 256 per log Mel audio clip
        # Parameters: 256*512 + 512*80 + 80*50 = ~176k 
        self.net = nn.Sequential(
            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(512, 80),
            nn.BatchNorm1d(80),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(80, 50)
        )
        
    def forward(self, x): 
        # x is (Batch, 128, 108)
        x_mean = x.mean(dim=2)
        x_std = x.std(dim=2)
        x_pooled = torch.cat([x_mean, x_std], dim=1) # Shape: (Batch, 256)
        return self.net(x_pooled)

class CNN1D(nn.Module):
    def __init__(self):
        super().__init__()
        # Deeper Sequence processing. Treats time as length and Mels as channels.
        # Params: (128*256*5) + (256*128*3) + (128*50) = ~163k params
        self.net = nn.Sequential(
            nn.Conv1d(128, 256, kernel_size=5, padding=2),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Conv1d(256, 128, kernel_size=3, padding=1),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1), # Global average pool across time
            nn.Flatten(),
            nn.Dropout(0.3),
            nn.Linear(128, 50)
        )
        
    def forward(self, x): return self.net(x)

class CNN2D(nn.Module):
    def __init__(self):
        super().__init__()
        # Deep image processing over spectrograms
        # Params: (1*16*3*3) + (16*64*3*3) + (64*128*3*3) + (128*50) = ~89k param
        self.net = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2),
            
            nn.Conv2d(16, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),
            
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, 1)), # Summarize frequency + time map
            
            nn.Flatten(),
            nn.Dropout(0.3),
            nn.Linear(128, 50)
        )
        
    def forward(self, x): 
        # Add single channel index for vision Conv dimensions
        return self.net(x.unsqueeze(1))
