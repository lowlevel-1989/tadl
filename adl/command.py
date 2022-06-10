from enum import Enum, auto
from dataclasses import dataclass
from dataclasses import field

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
    script   : list[int] = field(repr=False, default_factory=list)
