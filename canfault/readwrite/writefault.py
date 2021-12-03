from canlib import canlib, Frame

def write(channel, frame, func = None, params = []):
    """Writes Frames to a channel and optionally runs them through a function.
 
    :param channel: the channel from whtch the frames are read
    :type channel: canlib.Channel
    :param frame: the frame to send on channel
    :type frame: canlib.Frame
    :param func: the functions to run the Frames through, defaults to None
    :type func: callable, optional
    :param params: list of parametes to pass to func, defaults to []
    :type params: list, optional
    :raises TypeError: if parameters are of the wrong type
    """
    if(not isinstance(frame, Frame)):
        if(not isinstance(frame, list)):
            raise TypeError("The passed frame is not a canlib Frame!")
        else:
            for single_frame in frame:
                if(not isinstance(single_frame, Frame)):
                    raise TypeError("The passed frame is not a canlib Frame!")
    if(not isinstance(channel, canlib.channel.Channel)):
        raise TypeError("The passed frame is not a canlib Frame!")
    if(func is None):
        frame_fault = frame
    else:
        frame_fault = func(frame, params)
    if(frame_fault is not None):
        if(isinstance(frame_fault, list)):
            for single_frame in frame_fault:
                channel.write(single_frame)
        else:
            channel.write(frame_fault)
