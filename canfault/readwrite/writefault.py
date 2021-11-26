from canlib import canlib, Frame

def write(channel, frame, func = None, params = []):
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
