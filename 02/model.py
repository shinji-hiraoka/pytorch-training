import torch
import torch.nn as nn

class MyModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.mytensor = torch.full((3, 3), 2.0)
        self.elem_add = 4.0
        self.elem_multiply = 6.0

    def forward(self, x):
        x = x + self.mytensor
        x = x + self.elem_add
        x = x * self.elem_multiply

        return x