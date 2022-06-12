import sys
import io
from os.path import exists

sys.path.append("..")

from adl.command import Command

# direccion encontrada por scummvm
HR1_OFS_CMDS_0 = 0x3c00

def read8(buf : io.BufferedReader) -> int:
    return ord(buf.read(1))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        err(1, f"Usage: {sys.argv[0]} <file_input>")

    file_in  : str = sys.argv[1]

    if not exists(file_in):
        sys.exit(2)

    stream_in  : io.BufferedReader

    stream_in  = open(file_in,  "rb")

    stream_in.seek(HR1_OFS_CMDS_0)

    read8(stream_in)
    read8(stream_in)
    read8(stream_in)
    read8(stream_in)

    byte : bytes

    while 1:

        room : int = read8(stream_in)
        if room == 0xff:
            break

        command : Command = Command()

        command.id_room   = room
        command.verb      = read8(stream_in)
        command.noun      = read8(stream_in)

        script_len : int  = read8(stream_in) - 6

        command.num_cond  = read8(stream_in)
        command.num_act   = read8(stream_in)

        for _ in range(script_len):
            command.script.append(read8(stream_in))

        # only debug
        print(command)

    stream_in.close()
