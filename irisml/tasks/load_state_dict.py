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

    @dataclasses.dataclass
    class Outputs:
        model: torch.nn.Module = None

    def execute(self, inputs: Inputs):
        state_dict = torch.load(self._config.path, map_location='cpu')
        inputs.model.load_state_dict(state_dict)
        return self.Outputs(model=inputs.model)
