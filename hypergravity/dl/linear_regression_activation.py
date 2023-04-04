import matplotlib.pyplot as plt
import numpy as np
import torch

# truth
n_sample = 1000
n_dim = 1

# generate data sample
X_data = torch.rand(size=(n_sample, n_dim))
y_data = 3 * torch.sin(X_data * 20) + 10
print(X_data.shape, y_data.shape)
y_data = y_data.reshape(-1, 1)

# to visualize X and y
ax = plt.figure().add_subplot()
ax.scatter(X_data.numpy(), y_data.numpy())
ax.set_xlabel("Feature 0")
ax.set_ylabel("Label")

# below goes new code
from torch.utils import data


def load_array(data_arrays, batch_size, is_train=True):
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)


batch_size = 10
data_iter = load_array((X_data, y_data), batch_size)  # a DataLoader

# define model
net = torch.nn.Sequential(
    torch.nn.Linear(in_features=1, out_features=10, bias=True),
    torch.nn.Tanh(),
    torch.nn.Linear(in_features=10, out_features=1, bias=True),
)
net[2].bias.data.fill_(10)

# define loss
loss = torch.nn.MSELoss()
# optimizer
trainer = torch.optim.Adam(net.parameters(), lr=0.01)

# train model
n_epoch = 3999
# loss_hist_tanh = np.zeros(n_epoch, dtype=float)
loss_hist_tanh_adam = np.zeros(n_epoch, dtype=float)
# loss_hist_sigmoid = np.zeros(n_epoch, dtype=float)
for epoch in range(n_epoch):
    for X, y in data_iter:
        l = loss(net(X), y)
        trainer.zero_grad()
        l.backward()
        trainer.step()
    l = loss(net(X_data), y_data)
    # loss_hist_tanh[epoch] = float(l)
    loss_hist_tanh_adam[epoch] = float(l)
    # loss_hist_sigmoid[epoch] = float(l)
    print(f"Epoch {epoch} - loss = {l}")

# to visualize X and y
ax = plt.figure().add_subplot()
ax.scatter(X_data.numpy(), y_data.numpy())
ax.scatter(X_data.numpy(), net(X_data).detach().numpy())
ax.set_xlabel("Feature 0")
ax.set_ylabel("Label")


ax = plt.figure().add_subplot()
ax.plot(np.log10(loss_hist_sigmoid), label="sigmoid [SGD]")
ax.plot(np.log10(loss_hist_tanh), label="tanh [SGD]")
ax.plot(np.log10(loss_hist_tanh_adam), label="tanh [Adam]")
ax.legend()
ax.set_xlabel("Epoch")
ax.set_ylabel("log10(loss)")
