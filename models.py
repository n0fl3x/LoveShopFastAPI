from enum import Enum, unique


class RandomSomething(str, Enum):
    random = "random"


@unique
class Categories(int, Enum):
    lubes = 1
    dildos = 2
    vibrators = 3
    giants = 4
    

@unique
class Items(int, Enum):
    water_based_lube = 1
    bodysuit = 2
    butt_plug = 3
    horse_cock = 4
