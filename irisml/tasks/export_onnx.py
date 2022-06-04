import dataclasses
import torch
import irisml.core


class Task(irisml.core.TaskBase):
    @dataclasses.dataclass
    class Inputs:
        model: torch.nn.Module

    @dataclasses.dataclass
    class Config:
        path: str

    def execute(self, inputs):
        pass
