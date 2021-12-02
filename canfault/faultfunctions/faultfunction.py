from canlib import canlib, Frame
from canlib.canlib import ChannelData
from bitarray import bitarray
from bitarray import util
import time
<<<<<<< HEAD
import logging

def bit_filler(frame_as_bits):
    bit_filler = bitarray(endian='big')
    bit_filler = util.zeros(8)
    while frame_as_bits.count(0) + frame_as_bits.count(1) < 64:
        frame_as_bits.extend(bit_filler)
    return frame_as_bits
=======
import random
>>>>>>> 624a1a66d8f30d2995156a0d97a6df707bedb5fe

def corrupt(frame, params = []):
    start = params[0]
    lenght = params[1]
    if start < 0 or lenght + start > 64:
        logging.error("Bad parameters start: %d lenght: %d", start, lenght)
    else:
        print("start {}  lenght {}". format(start, lenght))
        logging.info("start %d  lenght %d", start, lenght)
        frame_as_bytes = bytes(frame.data)

        if frame.data == None:
            frame_as_bits = util.zeros(64)
        else:
            frame_as_bits = bitarray(endian='big')
            frame_as_bits.frombytes(frame_as_bytes)
            frame_as_bits = bit_filler(frame_as_bits)

        for i in range(start, lenght + start):
            bitarray.invert(frame_as_bits, i)

        frame_as_bytes = frame_as_bits.tobytes()
        frame.data = frame_as_bytes
    return frame


def delay(frame, params =[]):
    time.sleep(params[0])
    return frame


def duplicate(frame, params = []):
    return [frame,frame]

_frame = None
_stored = 0

def set_stored(frame):
    global _stored
    global _frame
    if(_stored == 1):
        _stored = 0
        ret = _frame
        _frame = None
        return ret, 1
    else:
        _frame = frame
        _stored = 1
        return None, 0

def swap(frame, params = []):
    old_frame, stored = set_stored(frame)
    if(stored == 1):
        return [frame, old_frame]
    else:
        return old_frame
<<<<<<< HEAD
=======

def insert(frame, params =[]):
    frame_id = random.randint(0, 1023)
    data = random.randint(2047, 8191)
    new_frame = Frame(frame_id, data, flags = canlib.MessageFlag.EXT)
    return[new_frame,frame]
>>>>>>> 624a1a66d8f30d2995156a0d97a6df707bedb5fe
