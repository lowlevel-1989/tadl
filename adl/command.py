import sys

from enum import Enum, auto
from dataclasses import dataclass

if __name__ == "__main__":
    from common.misc import ListBytes
else:
    from adl.common.misc import ListBytes

class OP_TYPE(Enum):
    DONE = auto()
    COND = auto() # opcode condicional
    ACT  = auto() # opcode acción

@dataclass
class Command:
    id_room  : int
    verb     : int # verbo
    noun     : int # sustantivo
    num_cond : int
    num_act  : int
    script   : ListBytes[int]

    def __init__(self) -> None:
        self.script = ListBytes()
