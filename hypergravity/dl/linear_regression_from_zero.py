import matplotlib.pyplot as plt
import numpy as np
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

# to visualize X and y
ax = plt.figure().add_subplot(projection='3d')
ax.scatter(X_data[:, 0].numpy(), X_data[:, 1].numpy(), y_data.numpy())
ax.set_xlabel("Feature 0")
ax.set_ylabel("Feature 1")
ax.set_zlabel("Label")


# define data generator
def data_iter(X, y, batch_size=100):
    n_sample = y.shape[0]

    indices = np.arange(n_sample)
    np.random.shuffle(indices)

    for i_batch in range(0, n_sample, batch_size):
        ind_batch = indices[i_batch:min(i_batch + batch_size, n_sample)]
        yield X[ind_batch], y[ind_batch]


for X, y in data_iter(X_data, y_data, batch_size=110):
    print(X.shape, y.shape, X[0], y[0])


# define model
def linear_regression(X, w, b):
    """

    Parameters
    ----------
    X:
        n_sample, n_dim
    w:
        n_dim, 1
    b:
        1,

    Returns
    -------

    """
    return torch.matmul(X, w) + b


# loss function
def squared_loss(y_hat, y):
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2


# optimizer
def sgd(params, lr, batch_size):
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()


# initialize parameters
w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
b = torch.zeros(size=(1,), requires_grad=True)

# define model hyperparameters
net = linear_regression
loss = squared_loss
lr = 0.01
n_epoch = 300
batch_size = 100

# train
for epoch in range(n_epoch):
    """ model itself is not important, loss & backward step are important!
    loss -> parameter gradients -> backward (update parameters)  
    """
    for X, y in data_iter(X_data, y_data, batch_size=batch_size):
        l = loss(net(X, w, b), y)  # (batch_size, 1)
        l.sum().backward()
        sgd([w, b], lr, batch_size=batch_size)
    """ when calculating training loss, use `with torch.no_grad()` context """
    with torch.no_grad():
        train_l = loss(net(X_data, w, b), y_data)  # (n_sample, 1)
        # print(train_l.shape)
        print(f"Epoch {epoch} - loss = {train_l.mean()}")

# compare parameters with truths
print(w_true, b_true)
print(w, b)
