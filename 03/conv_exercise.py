
import torch
import torch.nn as nn

# 問題1：32 × 3 × 128 × 128 のテンソルを作成
x = torch.ones(32, 3, 128, 128)
print("問題1:", x.shape)

# 問題2：32 × 64 × 126 × 126
conv2 = nn.Conv2d(
    in_channels=3,
    out_channels=64,
    kernel_size=3,
    stride=1,
    padding=0
)
y2 = conv2(x)
print("問題2:", y2.shape)

# 問題3：32 × 256 × 64 × 64
conv3 = nn.Conv2d(
    in_channels=3,
    out_channels=256,
    kernel_size=3,
    stride=2,
    padding=1
)
y3 = conv3(x)
print("問題3:", y3.shape)

# 問題4：kernel_size=5で同じ結果を得る

# 問題2と同じ形状
conv4_a = nn.Conv2d(
    in_channels=3,
    out_channels=64,
    kernel_size=5,
    stride=1,
    padding=1
)
y4_a = conv4_a(x)
print("問題4-1:", y4_a.shape)

# 問題3と同じ形状
conv4_b = nn.Conv2d(
    in_channels=3,
    out_channels=256,
    kernel_size=5,
    stride=2,
    padding=2
)
y4_b = conv4_b(x)
print("問題4-2:", y4_b.shape)
