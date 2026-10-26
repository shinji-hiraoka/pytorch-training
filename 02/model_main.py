import torch
from model import MyModel

if __name__ == "__main__":

    # モデルを作成
    model = MyModel()

    # 入力Tensor（3行3列、すべて1.0）
    x = torch.ones(3, 3)

    # モデルを実行
    output = model(x)

    print("入力Tensor:")
    print(x)

    print("出力Tensor:")
    print(output)