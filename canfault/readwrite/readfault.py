from canlib import canlib, Frame
from typing import Callable

""" Used to read from the bus if no frame is supplied.
 Used to pretend to read a frame from the bus if a frame is supplied.
 May be used when you want to inject faults in only one of the components
 connected to a bus with multiple components connected to it. 
"""
def read(channel, func = None, frame = None, params = []):
    """Reads Frames from a channel and optionally runs them through a function, returns the Frame.
 
    :param channel: the channel from whtch the frames are read
    :type channel: canlib.Channel
    :param func: the functions to run the Frames through, defaults to None
    :type func: callable, optional
    :param frame: if provided, this frame will be used instead of reading from channel, defaults to None
    :type frame: canlib.Frame, optional
    :param params: list of parametes to pass to func, defaults to []
    :type params: list, optional
    :raises TypeError: if parameters are of the wrong type
    
    :rtype: canlib.Frame, None
    :return: frame, None
    """
    if func is not None and not isinstance(func, Callable):
        raise(TypeError("The passed func is not a callable!"))
    if not isinstance(params, list):
        raise(TypeError("The passed params is not a list!"))
    if(frame is not None and not isinstance(frame, Frame)):
        raise TypeError("The passed frame is not a canlib Frame!")
    if(not isinstance(channel, canlib.channel.Channel)):
        raise TypeError("The channel is not a proper canlib Channel!")
    while True:
        try:
            if(frame is None):
                frame = channel.read()
            if(func is None):
                return frame
            return func(frame, params)
        except (canlib.canNoMsg) as ex:
            return None
    

            
