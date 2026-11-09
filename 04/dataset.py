
from pathlib import Path
from PIL import Image
from torch.utils.data import Dataset


class ImageDataset(Dataset):

    def __init__(self, data_dir):
        self.image_paths = sorted(
            Path(data_dir).rglob("*.png")
        )

    def __len__(self):
        # データセットの画像枚数
        return len(self.image_paths)

    def __getitem__(self, index):
        # 指定された画像を読み込む
        image_path = self.image_paths[index]

        with Image.open(image_path) as img:
            image = img.copy()

        # 親フォルダ名をラベルにする
        label = int(image_path.parent.name)

        return image, label


if __name__ == "__main__":

    # データフォルダの場所
    data_dir = (
        Path(__file__).resolve().parent
        / "exercise"
        / "data"
    )

    # データセットを作成
    dataset = ImageDataset(data_dir)

    # 問題1：データセットの枚数
    print("問題1:", len(dataset))

    # 問題2：画像サイズ
    image, label = dataset[0]

    print("問題2:", image.size)
    print("ラベル:", label)
