from enum import Enum, auto

class DIR(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST  = auto()
    WEST  = auto()
    UP    = auto()
    DOWN  = auto()
    TOTAL = auto()

class Room:
    __id              : int
    description_id    : int
    connections       : dict[DIR, int]
    is_first_time     : bool           = True

    @property
    def id(self) -> int:
        return self.__id

    def __init__(self, id, description_id) -> None:
        self.__id = id
        self.description_id = description_id
        self.connections = dict()

    def __repr__(self) -> str:
        o = f"{self.__class__.__name__}({self.id:02x}, description_id={self.description_id:02x}"
        o = f"{o}, is_first_time={self.is_first_time}"

        o = f"{o}, connections=| "
        for k, c in self.connections.items():
            o = f"{o}{k.name}:Room({c:02x}) | "

        # eliminar ultima coma
        l = len(o) - 2
        o = f"{o[:l]}|)"

        return o

# Esto es solo una prueba rapida (instancia una habitación)
if __name__ == "__main__":
    room = Room(id=1, description_id=1)
    room.connections[DIR.SOUTH] = 1
    room.connections[DIR.NORTH] = 200
    print(room)
