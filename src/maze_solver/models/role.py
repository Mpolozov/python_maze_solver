# models/role.py

from enum import IntEnum, auto

class Role(IntEnum):
    NA = 0
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()