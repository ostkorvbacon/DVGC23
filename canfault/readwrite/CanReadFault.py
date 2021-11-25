from canlib import canlib, Frame

""" Used to read from the bus if no frame is supplied.
 Used to pretend to read a frame from the bus if a frame is supplied.
 May be used when you want to inject faults in only one of the components
 connected to a bus with multiple components connected to it. 
"""
def read(channel, func = None, frame = None, params = []):
    if(frame is not None and not isinstance(frame, Frame)):
        raise TypeError("The passed frame is not a canlib Frame!")
    while True:
        try:
            if(frame is None):
                frame = channel.read()
            if(func is None):
                return frame
            return func(frame, params)
        except (canlib.canNoMsg) as ex:
            return None
    

            
