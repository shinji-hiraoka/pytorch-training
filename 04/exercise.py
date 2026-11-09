
from pathlib import Path

# 今回のdataフォルダを指定
data_dir = Path(__file__).resolve().parent / "exercise" / "data"

# 問題1：絶対パスを表示
print("問題1:", data_dir.resolve())

# 問題2：data配下のディレクトリをすべて表示
print("問題2:")
for path in sorted(data_dir.rglob("*")):
    if path.is_dir():
        print(path)

# 問題3：PNG画像ファイルの数を表示
png_files = list(data_dir.rglob("*.png"))
print("問題3:", len(png_files))
