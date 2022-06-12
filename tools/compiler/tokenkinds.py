from enum import Enum, auto

class TOKEN(enum):

    # token de un simple caracter
    DOT           = auto()   # .
    DOLLAR        = auto()   # $
    L_SQUARE      = auto()   # [
    R_SQUARE      = auto()   # ]

    # token de uno o dos caracteres
    EQUAL         = auto()   # =
    GREATER       = auto()   # >
    EQUAL_EQUAL   = auto()   # ==

    # literales
    IDENTIFIER    = auto()   # variable
    STRING        = auto()
    NUMBER        = auto()

    # palabras reservadas / keywords
    DAT           = auto()
    ROOM_SET      = auto()
    PRINT         = auto()

    # especiales
    SRC           = auto() # .SRC
    ROOM          = auto() # .ROOM
    COMMAND       = auto() # .COMMAND

    EOF           = auto()   # final de archivo
