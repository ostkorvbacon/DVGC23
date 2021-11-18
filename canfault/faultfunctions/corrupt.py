from canlib import canlib, Frame
from canlib.canlib import ChannelData
from bitarray import bitarray

def access_bit(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data[base] >> shift) & 0x1

def corrupt_frame(frame, params = []):
    #print(frame)
    #print(dir(bitarray))
    i=0
    temp = [access_bit(frame.data,i) for i in range(len(frame.data)*8)]
    print(temp)

    temp3 = bytes(frame.data)
    temp2 = bitarray(endian='big')
    temp2.frombytes(temp3)
    print(temp2)
    bitarray.invert(temp2)
    print("invertetd", format(temp2))
    return frame
