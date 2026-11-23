
from pathlib import Path
from PIL import Image
from torchvision import transforms

# 前回使用した画像を読み込む
data_dir = Path(__file__).resolve().parent.parent / "04" / "exercise" / "data"
image_path = sorted(data_dir.rglob("*.png"))[0]

image = Image.open(image_path).convert("RGB")

# 問題1：リサイズと正規化
transform1 = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.5, 0.5, 0.5],
        std=[0.5, 0.5, 0.5]
    )
])

# 問題2：ランダムな水平反転と色調変換
transform2 = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.ColorJitter(
        brightness=0.3,
        contrast=0.3,
        saturation=0.3,
        hue=0.1
    ),
    transforms.ToTensor()
])

# 問題3：ランダムな回転とクロップ
transform3 = transforms.Compose([
    transforms.RandomRotation(degrees=30),
    transforms.RandomCrop(size=(24, 24), pad_if_needed=True),
    transforms.ToTensor()
])

# 各変換を実行
output1 = transform1(image)
output2 = transform2(image)
output3 = transform3(image)

# 結果を表示
print("問題1:", output1.shape)
print("問題2:", output2.shape)
print("問題3:", output3.shape)

# Tensorになっているか確認
print("問題1の型:", type(output1))
print("問題2の型:", type(output2))
print("問題3の型:", type(output3))
