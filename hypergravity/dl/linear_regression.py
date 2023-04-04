import matplotlib.pyplot as plt
# import numpy as np
import torch

# truth
w_true = torch.tensor([2, -3.4])
b_true = torch.tensor(4.2)
n_sample = 1000
n_dim = len(w_true)

# generate data sample
X_data = torch.normal(0, 1, (n_sample, n_dim))
y_data = torch.matmul(X_data, w_true) + b_true
print(X_data.shape, y_data.shape)
y_data = y_data.reshape(-1, 1)

# to visualize X and y
ax = plt.figure().add_subplot(projection='3d')
ax.scatter(X_data[:, 0].numpy(), X_data[:, 1].numpy(), y_data.numpy())
ax.set_xlabel("Feature 0")
ax.set_ylabel("Feature 1")
ax.set_zlabel("Label")

# below goes new code
from torch.utils import data


def load_array(data_arrays, batch_size, is_train=True):
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)


batch_size = 100
data_iter = load_array((X_data, y_data), batch_size)  # a DataLoader

# define model
net = torch.nn.Sequential(
    torch.nn.Linear(in_features=2, out_features=1, bias=True)
)
# initialize parameters
net[0].weight.data.normal_(0, 0.01)
net[0].bias.data.fill_(0)

# define loss
loss = torch.nn.MSELoss()
# optimizer
trainer = torch.optim.SGD(net.parameters(), lr=0.03)

# train model
n_epoch = 30
for epoch in range(n_epoch):
    for X, y in data_iter:
        l = loss(net(X), y)
        trainer.zero_grad()
        l.backward()
        trainer.step()
    l = loss(net(X_data), y_data)
    print(f"Epoch {epoch} - loss = {l}")

print(net.state_dict())
