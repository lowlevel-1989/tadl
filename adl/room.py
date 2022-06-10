from enum import Enum, auto
from dataclasses import dataclass
from dataclasses import field

from common.field import ImmutableID

class DIR(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST  = auto()
    WEST  = auto()
    UP    = auto()
    DOWN  = auto()
    TOTAL = auto()

class RoomID(ImmutableID):
    pass

class DescriptionID(ImmutableID):
    def __repr__(self) -> str:
        return "{:d}".format(self.get_id())

@dataclass
class Room:
    description_id : DescriptionID
    connections    : dict[DIR, RoomID] = field(default_factory=dict)
    is_first_time  : bool      = True

if __name__ == "__main__":
    room = Room(DescriptionID(0))
    room.connections[DIR.SOUTH] = RoomID(1)
    print(room)
