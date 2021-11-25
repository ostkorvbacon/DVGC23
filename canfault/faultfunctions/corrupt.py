from canlib import canlib, Frame
from canlib.canlib import ChannelData
from bitarray import bitarray
from bitarray import util


def corrupt(frame, params = []):
    start = params[0]
    lenght = params[1]
    if start < 0 or lenght + start > 64:
        print("Bad parameters")

    else:
        print("start {}  lenght {}". format(start, lenght))
        frame_as_bytes = bytes(frame.data)

        if frame.data == None:
            frame_as_bits = util.zeros(64)
        else:
            frame_as_bits = bitarray(endian='big')
            frame_as_bits.frombytes(frame_as_bytes)
            bit_filler = bitarray(endian='big')
            bit_filler = util.zeros(8)
            while frame_as_bits.count(0) + frame_as_bits.count(1) < 64:
                frame_as_bits.extend(bit_filler)

        print("Normal   ", format(frame_as_bits))
        for i in range(start, lenght):
            bitarray.invert(frame_as_bits, i)

        print("invertetd", format(frame_as_bits))
        frame_as_bytes = frame_as_bits.tobytes()
        frame.data = frame_as_bytes
    return frame
