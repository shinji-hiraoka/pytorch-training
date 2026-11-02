
import torch
from models import MyModel

if __name__ == "__main__":

    # 入力Tensor
    x = torch.ones(32, 3, 128, 128)

    # モデル作成
    model = MyModel()

    # モデル実行
    output = model(x)

    print("入力:", x.shape)
    print("出力:", output.shape)
