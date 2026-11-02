
import torch
import torch.nn as nn

class MyModel(nn.Module):

    def __init__(self):
        super().__init__()

        # Convolution
        self.conv = nn.Conv2d(
            in_channels=3,
            out_channels=256,
            kernel_size=5,
            stride=8,
            padding=2
        )

        # Batch Normalization
        self.bn = nn.BatchNorm2d(256)

        # ReLU
        self.relu = nn.ReLU()

        # Linear
        self.fc = nn.Linear(256 * 16 * 16, 64)

    def forward(self, x):

        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)

        # 全結合層に渡すために平坦化
        x = torch.flatten(x, start_dim=1)

        x = self.fc(x)

        return x
