import dataclasses
import typing
import torch

import irisml.core


class Task(irisml.core.TaskBase):
    @dataclasses.dataclass
    class Config:
        num_epoch: int

    @dataclasses.dataclass
    class Inputs:
        train_dataset: torch.utils.data.Dataset
        val_dataset: torch.utils.data.Dataset
        train_transform: typing.Callable
        val_transform: typing.Callable
        model: torch.nn.Module

    @dataclasses.dataclass
    class Outputs:
        model: torch.nn.Module = None

    def execute(self, inputs):
        pass
