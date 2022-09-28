import json
from typing import List


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Agent:
    def __init__(self, position: Position):
        self.position = position


class Obstacle:
    def __init__(self, position: Position, type: str):
        self.position = Position
        self.type = type


class Defaults:
    agents = []
    obstacles = []

    def __init__(self, agents: List[Agent], obstacles: List[Obstacle]):
        self.agents = agents
        self.obstacles = obstacles

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __str__(self):
        return f'agents: {self.agents}, obstacle: {self.obstacles}'


def load_defaults(defaults_file: str) -> Defaults:
    """
    Returns loaded defaults
    :rtype: Defaults
    """
    with open(defaults_file, "r") as json_file:
        data = json.loads(json_file.read())
        return Defaults(**data)
