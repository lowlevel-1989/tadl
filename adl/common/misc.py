class ListBytes(list):
    def __repr__(self) -> str:
        o : str = "["
        for x in self:
            o = "%s %02x" % (o, x)

        o += " ]"
        return o
