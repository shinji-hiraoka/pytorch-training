
from pathlib import Path
from PIL import Image

# データフォルダを指定
data_dir = Path(__file__).resolve().parent / "exercise" / "data"

# PNG画像をすべて取得
image_files = sorted(data_dir.rglob("*.png"))

# 画像サイズとラベルを表示
for image_path in image_files:

    # 画像を読み込む
    with Image.open(image_path) as img:
        image_size = img.size

    # 親ディレクトリ名をラベルとして取得
    label = image_path.parent.name

    print(f"画像: {image_path.name}")
    print(f"サイズ: {image_size}")
    print(f"ラベル: {label}")
    print("--------------------")
