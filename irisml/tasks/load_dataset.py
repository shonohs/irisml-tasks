import dataclasses
import torch
import irisml.core


class Task(irisml.core.TaskBase):
    @dataclasses.dataclass
    class Inputs:
        path: str

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset = None
        num_classes: int = 0

    def execute(self, inputs):
        pass
