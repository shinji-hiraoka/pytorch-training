
from pathlib import Path
from torchvision import datasets, transforms

# 画像をTensorに変換
transform = transforms.ToTensor()

# CIFAR-10の訓練データを読み込む
data_dir = Path(__file__).resolve().parent / "data"

train_dataset = datasets.CIFAR10(
    root=str(data_dir),
    train=True,
    download=True,
    transform=transform
)

# 1枚目の画像とラベルを取得
image, label = train_dataset[0]

print("データ数:", len(train_dataset))
print("画像サイズ:", image.shape)
print("ラベル:", label)
