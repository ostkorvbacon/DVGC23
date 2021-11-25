from canlib import canlib, Frame
from canlib.canlib import ChannelData
from bitarray import bitarray


def corrupt(frame, params = []):
    start = params[0]
    lenght = params[1]
    if start < 0 or lenght + start > 24:
        print("Bad parameters")
    else:
        print("start {}  lenght {}". format(start, lenght))
        frame_as_bytes = bytes(frame.data)
        frame_as_bits = bitarray(endian='big')
        frame_as_bits.frombytes(frame_as_bytes)
        print("Normal   ", format(frame_as_bits))

        for i in range(start, lenght):
            bitarray.invert(frame_as_bits, i)

        print("invertetd", format(frame_as_bits))

    return frame
