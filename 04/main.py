
from pathlib import Path

# dataディレクトリを指定
data_dir = Path(__file__).resolve().parent / "data"

# 問題1：絶対パスを表示
print("問題1：", data_dir.resolve())

# 問題2：配下のディレクトリをすべて表示
print("問題2：")
for path in data_dir.rglob("*"):
    if path.is_dir():
        print(path)

# 問題3：PNG画像の数を表示
png_files = list(data_dir.rglob("*.png"))
print("問題3：", len(png_files))
