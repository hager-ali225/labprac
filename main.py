import torch
import torch.nn as nn

# Simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)


def main():
    model = SimpleModel()

    # dummy input
    x = torch.randn(1, 9)

    # forward pass
    output = model(x)

    print("Model is working fine!")
    print("Output:", output)


if __name__ == "__main__":
    main()
