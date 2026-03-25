import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np                
import matplotlib.pyplot as plt

# Device GPU or CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Create the input and validation data
x = torch.tensor([[6,2],[5,2],[1,3],[7,6]]).float()
y = torch.tensor([1,5,2,5]).float()

class tryNN2(nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = nn.Linear(2,80,bias=False)
        self.mat2 = nn.Linear(80,80)
        self.mat3 = nn.Linear(80,1,bias=False)
        self.relu = nn.ReLU()
        
    # Here mat x is the input data
    def forward(self, x):
        x = self.mat1(x)
        x = self.relu(x)
        x = self.mat2(x)
        x = self.relu(x)
        x = self.mat3(x)
        return x.squeeze()

# training
def train_model(x, y, f, n_epoch):
    opt = torch.optim.SGD(f.parameters(), lr=0.001)
    L = nn.MSELoss()
    
    losses = []
    for epochs in range(n_epoch):
        opt.zero_grad()
        loss_value = L(f(x), y)
        loss_value.backward()
        opt.step()
        losses.append(loss_value.item())
    return f, losses

# Data input and labels
x = torch.tensor([[6,2],[5,2],[1,3],[7,6]]).float().to(device)
y = torch.tensor([1,5,2,5]).float().to(device)
f2 = tryNN2().to(device)

# Training
f2, losses = train_model(x, y, f2, n_epoch=5000)
y_computed = f2(x)
print('y_computed by NN:', y_computed)
print('Original validation output Y:', y)

# Saving the trained model
quant_model = tryNN2().to(device)
torch.save(quant_model.state_dict(), 'linear_nn_relu.pt')