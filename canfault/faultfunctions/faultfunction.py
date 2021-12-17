from canlib import canlib, Frame
from canlib.canlib import ChannelData
from bitarray import bitarray
from bitarray import util
import time
import logging
import random

_frame = None
_stored = 0


def set_stored(frame):
    """Stores a Frame for swap, returns the frame if a frame is stored otherwise None.

    :param frame: canlib Frame to be stored
    :type frame: canlib.Frame

    :rtype: canlib.Frame or None
    :return: frame or None
    """
    logging.debug("Start")
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
        logging.debug("End")
        return None, 0

def bit_filler(frame_as_bits = bitarray("0000 0000")):
    """Fills out a bitarray with zeros untill it is 64 bits long

    :param frame_as_bits: bitarray to fill out
    :type frame_as_bits: bitarray

    :rtype: bitarray
    :return: frame_as_bits
    """
    logging.debug("Start")
    bit_filler = bitarray(endian ='big')
    bit_filler = util.zeros(8)
    while frame_as_bits.count(0) + frame_as_bits.count(1) < 64:
        frame_as_bits.extend(bit_filler)
    logging.debug("End")
    return frame_as_bits

def corrupt(frame, params=[]):
    """Corrupts a number of bits after/including a start bit

    :param frame: canlib Frame to be corupted
    :type frame: canlib.Frame
    :param params: first number is start bit for coruption, second number is amount of bits to be corupted
    :type params: list with first element as int, optional

    :rtype: canlib.Frame
    :return: frame
    """
    logging.debug("Start")
    start = params[0]
    lenght = params[1]
    if start < 0 or lenght + start > 64:
        logging.error("Bad parameters start: %d lenght: %d", start, lenght)
    else:
        print("start {}  lenght {}". format(start, lenght))
        logging.info("Parameters: start %d  lenght %d", start, lenght)
        if(frame.data is None):
            frame_as_bits = util.zeros(64)
            logging.error("There was no data in the frame.")
        else:
            frame_as_bytes = bytes(frame.data)
            frame_as_bits = bitarray(endian='big')
            frame_as_bits.frombytes(frame_as_bytes)
            frame_as_bits = bit_filler(frame_as_bits)
        for i in range(start, lenght + start):
            bitarray.invert(frame_as_bits, i)
        frame_as_bytes = frame_as_bits.tobytes()
        frame.data = frame_as_bytes
    logging.debug("End")
    return frame

def delay(frame, params=[]):
    """Delays a Frame by a number of seconds, returns the Frame.

    :param frame: canlib Frame to be delayed
    :type frame: canlib.Frame
    :param params: first element is time to delay in seconds, defaults to 0.1
    :type params: list with first element as int, optional

    :rtype: canlib.Frame
    :return: frame
    """
    logging.debug("Start")
    if(len(params) == 0):
        t = 0.1
    else:
        t = params[0]
    time.sleep(t)
    logging.debug("End")
    return frame

def duplicate(frame, params=[]):
    """Returns a number of copies of a Frame.

    :param frame: canlib Frame to be copied
    :type frame: canlib.Frame
    :param params: first element is number of copies, defaults to 2
    :type params: list with first element as int, optional

    :rtype: list
    :return: [frame * params[0]]
    """
    logging.debug("Start")
    f_list = []
    if(len(params) == 0):
        amount = 2
    else:
        amount = params[0]
    for _ in range(0, amount):
        f_list.append(frame)
    logging.debug("End")
    return f_list

def swap(frame, params=[]):
    """Swaps the order of two Frames and returns them in a list.

    :param frame: canlib Frame to be swaped
    :type frame: canlib.Frame
    :param params: not used, defaults to []
    :type params: optional

    :rtype: list
    :return: [frame, old_frame]
    """
    logging.debug("Start")
    old_frame, stored = set_stored(frame)
    if(stored == 1):
        logging.debug("End")
        return [frame, old_frame]
    else:
        logging.debug("End")
        return old_frame

def insert(frame, params=[]):
    """Inserts a Frame with random id and data.

    :param frame: canlib Frame to follow the inserted frame
    :type frame: canlib.Frame
    :param params: not used, defaults to []
    :type params: optional

    :rtype: list
    :return: [new_frame, frame]
    """
    logging.debug("Start")
    frame_id = random.randint(0, 1023)
    data = random.randint(0, 255)
    new_frame = Frame(frame_id, [data],dlc=8 ,flags=canlib.MessageFlag.EXT)
    logging.debug("End")
    
    #print(new_frame,frame, "hej")

    return[new_frame, frame]

def drop(frame,params=[]):
    """Drops the Frame it recives.

    :param frame: canlib Frame to follow the inserted frame
    :type frame: canlib.Frame
    :param params: not used, defaults to []
    :type params: optional

    :rtype: None
    :return: None
    """
    return None
