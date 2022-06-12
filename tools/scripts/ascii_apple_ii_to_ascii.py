import sys
import io
from os.path import exists

#  apple ii, us ascii 7 bit
#
#  127 == 0111 1111b
def encode_ascii(x : bytes) -> bytes:
    return (ord(x) & 127).to_bytes(1, "little")

def unicode_ascii(x : bytes) -> int:
    return ord(encode_ascii(x))

def char_ascii(x : bytes) -> str:
    return chr(unicode_ascii(x))

def err(code : int, message : str) -> None:
    print(message, file=sys.stderr)
    sys.exit(code)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        err(1, f"Usage: {sys.argv[0]} <file_input> <file_output>")

    file_in  : str = sys.argv[1]
    file_out : str = sys.argv[2]

    if not exists(file_in):
        sys.exit(2)

    stream_in  : io.BufferedReader
    stream_out : io.BufferedWriter

    stream_in  = open(file_in,  "rb")
    stream_out = open(file_out, "wb")

    byte : bytes = stream_in.read(1)

    while byte and char_ascii(byte) != "\0":

        # only debug
        val : str = char_ascii(byte)
        print(val, end="")
        if val == "\r":
            print()

        # save
        stream_out.write(encode_ascii(byte))
        if val == "\r":
            stream_out.write(b"\n")

        # next
        byte = stream_in.read(1)

    stream_in.close()
    stream_out.close()
