import torch

# 2行3列のTensorを作成
tensor = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

print("元のTensor:")
print(tensor)

# 形状の確認
print("shape:", tensor.shape)
print("size:", tensor.size())

# 軸の入れ替え
transposed = tensor.permute(1, 0)

print("軸入れ替え後:")
print(transposed)

print("変更後のshape:", transposed.shape)