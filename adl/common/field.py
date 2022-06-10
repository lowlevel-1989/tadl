class ImmutableID:
    def __init__(self, __id : int):
        self.__id = __id

    def get_id(self) -> int:
        return self.__id

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__id})"

