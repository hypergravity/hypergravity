import matplotlib.pyplot as plt
import torch.nn
import torchvision
from torch.utils import data


# get dataset
def load_data_fashion_mnist(batch_size, resize=None):
    # define transform
    trans = [torchvision.transforms.ToTensor()]
    if resize:
        trans.insert(0, torchvision.transforms.Resize(resize))
    trans = torchvision.transforms.Compose(trans)
    # dataset
    mnist_train = torchvision.datasets.FashionMNIST(
        root="hypergravity/data", train=True, transform=trans, download=True
    )
    mnist_test = torchvision.datasets.FashionMNIST(
        root="hypergravity/data", train=False, transform=trans, download=True
    )
    return (
        data.DataLoader(mnist_train, batch_size, shuffle=True, num_workers=4),
        data.DataLoader(mnist_test, batch_size, shuffle=True, num_workers=4),
    )


train_iter, test_iter = load_data_fashion_mnist(batch_size=32, resize=64)
for X, y in train_iter:
    print(X.shape, X.dtype, y.shape, y.dtype)
    break

# define model
net = torch.nn.Sequential(
    torch.nn.Flatten(),
    torch.nn.Linear(784, 10)
)


def init_weights(m):
    if type(m) == torch.nn.Linear:
        torch.nn.init.normal_(m.weight, mean=0., std=0.01)


net.apply(init_weights)

# define loss
loss = torch.nn.CrossEntropyLoss(reduction="none")

# define optimizer
trainer = torch.optim.SGD(net.parameters(), lr=0.01)

# train network
for epoch in range(1000):
    # train
    pass


def get_fashion_mnist_labels(labels):
    text_labels = ["t_shirt", "trouser", "pullover", "dress", "coat",
                   "sandal", "shirt", "sneaker", "bag", "ankle boot"]
    return [text_labels[int(i)] for i in labels]

# X, y = next(iter(data.DataLoader(mnist_train, batch_size=10)))
# print(X.shape, y.shape)

# ax = plt.figure().add_subplot()
# ax.imshow(X[1][0])
# ax.set_title(y[1])
