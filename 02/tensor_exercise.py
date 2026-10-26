import numpy as np
import torch

# 3クラス、各5人、2科目の点数
data = np.array([
    [[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
    [[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
    [[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]
])

# 問題1：NumPy配列をTensorに変換
tensor = torch.tensor(data, dtype=torch.float32)

print("元の形状:", tensor.shape)

# 問題2：2科目、3クラス、各5人に並び替える
subjects_first = tensor.permute(2, 0, 1)

print("並び替え後の形状:", subjects_first.shape)
print(subjects_first)
# 問題3：各生徒の2科目合計点
student_totals = subjects_first.sum(dim=0)
print("各生徒の合計点:")
print(student_totals)

# 問題4：クラスごとの平均点
class_averages = student_totals.mean(dim=1)
print("クラスごとの平均点:")
print(class_averages)

# 問題5：meanを使わず平均点を計算
class_averages2 = student_totals.sum(dim=1) / student_totals.shape[1]
print("meanを使わない平均点:")
print(class_averages2)

# 結果が一致するか確認
print("一致:", torch.allclose(class_averages, class_averages2))