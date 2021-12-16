from canlib import canlib, kvadblib
from canlib.kvadblib import Message
from canlib.canlib import ChannelData
from readwrite import writefault, readfault
from . import faultfunction
from environment import printframe
import logging
import random
from bitarray import bitarray
import numpy
import struct

from canlib.kvadblib.signal import Signal

def corrupt_signal_data(data, bit):
    """
    Function flipping a random bit of the signal data.

    :param data: The data to be corrupted.
    :type data: bytearray
    :param bit: The index of the bit to be corrupted
    :type bit: int

    :return: The corrupted data
    :rtype: bytearray
    """
    data_as_bytes = bytes(data)
    data_as_bits = bitarray(endian='big')
    data_as_bits.frombytes(data_as_bytes)

    bitarray.invert(data_as_bits, bit)

    data_as_bytes = data_as_bits.tobytes()
    data = data_as_bytes

    return data

def corrupt_signal(signal_name, database, channel):
    """
    Function for corrupting a random bit in the frame.

    :param database: Dbc where to look for the signal
    :type database: kvadblib.Dbc
    :param signal: Name of the signal to be corrupted
    :type signal_name: String

    :return: The corrupted signal
    :rtype: kvadblib.Signal
    """
    frame = channel.read()
    bound_message = database.interpret(frame)
    signal = ''
    for message in database.messages():
        for signal_instance in message.signals():
            if signal_instance.name == signal_name:
                signal = signal_instance
                message_corrupt = message
    
    for signals in bound_message:
        if signals.name == signal_name:
            signal = signals

    start = signal.signal.size.startbit
    length = signal.signal.size.length

    data = frame.data
    
    flip_bit = random.randint(start, start+length-1)
    print(start)
    print(length)
    print(flip_bit)
    print(data)
    new_data = corrupt_signal_data(data, flip_bit)
    print(new_data)
    
    return frame


    