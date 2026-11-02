
import torch
import torch.nn as nn

# 問題1：32 × 1024 のテンソルを作成
x = torch.ones(32, 1024)
print("問題1:", x.shape)

# 問題2：32 × 256 に変換
linear1 = nn.Linear(
    in_features=1024,
    out_features=256
)
y1 = linear1(x)
print("問題2:", y1.shape)

# 問題3：32 × 2048 に変換
linear2 = nn.Linear(
    in_features=1024,
    out_features=2048
)
y2 = linear2(x)
print("問題3:", y2.shape)

# Appendix：問題2の出力を32 × 16 × 16に変形
y3 = y1.reshape(32, 16, 16)
print("Appendix:", y3.shape)
