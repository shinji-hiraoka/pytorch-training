
import torch
import torch.nn as nn


class CNN(nn.Module):
    def __init__(self):
        super().__init__()

        # 畳み込み層
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)

        # プーリング層
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        # 活性化関数
        self.relu = nn.ReLU()

        # 全結合層
        self.fc1 = nn.Linear(64 * 8 * 8, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))

        x = torch.flatten(x, 1)

        x = self.relu(self.fc1(x))
        x = self.fc2(x)

        return x


if __name__ == "__main__":
    model = CNN()
    x = torch.ones(32, 3, 32, 32)

    output = model(x)

    print("入力:", x.shape)
    print("出力:", output.shape)
