import dataclasses
from typing import List
import irisml.core


class Task(irisml.core.TaskBase):
    @dataclasses.dataclass
    class Config:
        transforms: List[str]

    def execute(self, inputs):
        # TODO
        pass
