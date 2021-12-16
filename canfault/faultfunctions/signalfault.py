from canlib import canlib, kvadblib
from canlib.kvadblib import Message
from canlib.canlib import ChannelData
from readwrite import writefault, readfault
from . import faultfunction
from environment import printframe
import logging
import random
from bitarray import bitarray

from canlib.kvadblib.signal import Signal

def load_corrupt(frame, bit):
    printframe.print_frame(frame)
    frame_as_bytes = bytes(frame.data)
    frame_as_bits = bitarray(endian='big')
    frame_as_bits.frombytes(frame_as_bytes)

    bitarray.invert(frame_as_bits, bit)

    frame_as_bytes = frame_as_bits.tobytes()
    frame.data = frame_as_bytes

    return frame

def corrupt_message(frame, params):
    """
    Function for corrupting a random bit in the frame.

    
    :param params: [0] = Message name, [1] = signal name, [2] = db
    :type params: List

    :return: The corrupted frame
    :rtype: canlib.Frame
    """
    db = params[2]
    message = db.get_message_by_name(params[0])
    signal = message.get_signal(params[1])
    start = signal.size.startbit
    length = signal.size.length

    flip_bit = random.randint(start, start+length)
    print(start)
    print(length)
    print(flip_bit)
    #message.data = load_corrupt(message.data, flip_bit)
    '''for ... in database, For signals in frame. Leta upp alla signaler i en frame. Anta att namn  på signaler är unika. 
    parametrar in skall vara signal name och ev. databs. De har ett ramverk där databasen är tillgänglig så den behöver inte vara ett argument'''
    print("id")
    print(message)
    print(signal)
    
    return message.asframe()


    