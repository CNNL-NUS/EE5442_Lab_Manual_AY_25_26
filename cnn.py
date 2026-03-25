import torch
import torchvision
import torch.nn as nn
import torchvision.transforms as transforms

print("Starting...", flush=True)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Training on: {device}", flush=True)

l_r       = 0.001
n_epoch   = 5
n_datasets = 64
n_classes  = 10

transform_on_train_data = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.1307,), std=(0.3081,))
])
transform_on_test_data = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.1325,), std=(0.3105,))
])

data_train = torchvision.datasets.MNIST(
    root='./mnist', train=True,
    transform=transform_on_train_data, download=False)   # data must exist
data_test = torchvision.datasets.MNIST(
    root='./mnist', train=False,
    transform=transform_on_test_data,  download=False)

load_data_train = torch.utils.data.DataLoader(
    dataset=data_train, batch_size=n_datasets, shuffle=True)
load_data_test  = torch.utils.data.DataLoader(
    dataset=data_test,  batch_size=n_datasets, shuffle=True)

print("Data loaded.", flush=True)

class LeNet5_mnist(nn.Module):
    def __init__(self, num_classes):
        super(LeNet5_mnist, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 6, kernel_size=5, stride=1, padding=0),
            nn.BatchNorm2d(6),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(6, 16, kernel_size=5, stride=1, padding=0),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.fc    = nn.Linear(400, 120)
        self.relu  = nn.ReLU()
        self.fc1   = nn.Linear(120, 84)
        self.relu1 = nn.ReLU()
        self.fc2   = nn.Linear(84, num_classes)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc(out)
        out = self.relu(out)
        out = self.fc1(out)
        out = self.relu1(out)
        out = self.fc2(out)
        return out

model     = LeNet5_mnist(n_classes).to(device)
cost      = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=l_r)

total_step = len(load_data_train)
print(f"Training... {total_step} steps per epoch", flush=True)

for epoch in range(n_epoch):
    for i, (images, labels) in enumerate(load_data_train):
        images = images.to(device)
        labels = labels.to(device)
        #Forward pass
        outputs = model(images)
        loss    = cost(outputs, labels)
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (i + 1) % 100 == 0:
            print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'
                  .format(epoch+1, n_epoch, i+1, total_step, loss.item()), flush=True)

# Saving the trained model
torch.save(model.state_dict(), 'CNN_mnist.pt')
print("Model saved.", flush=True)

# Validate the model, check the accuracy of the trained model
# In test phase, we don't need to compute gradients (for memory efficiency)
with torch.no_grad():
    correct = 0
    total   = 0
    for images, labels in load_data_test:
        images = images.to(device)
        labels = labels.to(device)

        # Input the images to the trained model and store the outputs, then validate
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total   += labels.size(0)
        correct += (predicted == labels).sum().item()
    print('Accuracy: {} %'.format(100 * correct / total), flush=True)