import numpy as np
import torch

# 0で埋めたTensor
a = torch.zeros(3, 3)
print("zeros:")
print(a)

# 1で埋めたTensor
b = torch.ones(3, 3)
print("ones:")
print(b)

# 指定した値で埋めたTensor
c = torch.full((3, 3), 5)
print("full:")
print(c)

# NumPy配列を作成
array = np.array([0, 2, 5])

# メモリ共有
tensor1 = torch.from_numpy(array)

# メモリ非共有
tensor2 = torch.tensor(array)

# NumPy配列を変更
array[0] = 99

print("from_numpy:")
print(tensor1)

print("tensor:")
print(tensor2)