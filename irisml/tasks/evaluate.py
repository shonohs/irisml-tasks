import dataclasses
import typing
import torch
import irisml.core


class Task(irisml.core.TaskBase):
    @dataclasses.dataclass
    class Inputs:
        model: torch.nn.Module
        dataset: torch.utils.data.Dataset
        transform: typing.Callable

    def execute(self, inputs):
        pass
