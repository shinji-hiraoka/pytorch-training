
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from pathlib import Path

from model import CNN


def run_epoch(model, loader, criterion, optimizer=None):
    # optimizerがある場合は学習モード
    is_train = optimizer is not None
    model.train(is_train)

    total_loss = 0.0
    correct = 0
    total = 0

    for images, labels in loader:
        if is_train:
            optimizer.zero_grad()

        with torch.set_grad_enabled(is_train):
            outputs = model(images)
            loss = criterion(outputs, labels)

            if is_train:
                loss.backward()
                optimizer.step()

        total_loss += loss.item() * images.size(0)
        predictions = outputs.argmax(dim=1)
        correct += (predictions == labels).sum().item()
        total += labels.size(0)

    return total_loss / total, 100 * correct / total


if __name__ == "__main__":
    # データセットの準備
    data_dir = Path(__file__).resolve().parent / "data"

    transform = transforms.ToTensor()

    train_dataset = datasets.CIFAR10(
        root=str(data_dir),
        train=True,
        download=False,
        transform=transform
    )

    test_dataset = datasets.CIFAR10(
        root=str(data_dir),
        train=False,
        download=True,
        transform=transform
    )

    train_loader = DataLoader(
        train_dataset, batch_size=64, shuffle=True
    )

    test_loader = DataLoader(
        test_dataset, batch_size=64, shuffle=False
    )

    # モデル・損失関数・最適化関数
    model = CNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # 5エポック学習
    for epoch in range(5):
        train_loss, train_acc = run_epoch(
            model, train_loader, criterion, optimizer
        )

        test_loss, test_acc = run_epoch(
            model, test_loader, criterion
        )

        print(
            f"Epoch {epoch + 1}/5 | "
            f"Train Loss: {train_loss:.4f} | "
            f"Train Acc: {train_acc:.2f}% | "
            f"Test Loss: {test_loss:.4f} | "
            f"Test Acc: {test_acc:.2f}%"
        )
