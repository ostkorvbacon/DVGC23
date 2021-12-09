from canlib import canlib, kvadblib
from canlib.kvadblib import Message
from canlib.canlib import ChannelData
from readwrite import writefault, readfault
import faultfunction
import logging
import random

from canlib.kvadblib.signal import Signal

def corrupt_message(channel, params, readwrite_function):
    """
    Function for corrupting a random bit in the frame. .

    :param channel: Channel from which the frames are handled in the readwritefunction
    :type channel: canlib.channel.Channel
    :param params: [0] = Message name, [1] = signal name, [2] = db
    :type params: List
    :param readwrite_function: Either readwrite.readfault.read() or readwrite.writefault.write depending on where the fault is to be injected.
    :type readwrite_function: Callable

    :return: The corrupted message
    :rtype: canlib.kvadblib.Message
    """
    db = params[2]
    message = db.get_message_by_name(params[0])
    bound = message.bind()
    signal = message.get_signal(params[1])
    start = signal.size.startbit
    length = signal.size.length

    flip_bit = random.randint(start, length)
    corrupt_params = [flip_bit, 1]
    bound._frame = readwrite_function(channel, bound._frame, faultfunction.corrupt, corrupt_params)

    return message


    