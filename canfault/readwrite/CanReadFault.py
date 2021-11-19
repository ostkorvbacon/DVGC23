from canlib import canlib

""" Used to read from the bus if no frame is supplied.
 Used to pretend to read a frame from the bus if a frame is supplied.
 May be used when you want to inject faults in only one of the components
 connected to a bus with multiple components connected to it. 
"""
def read(channel, func = None, frame = None, params = []):
    while True:
        try:
            if(func == None):
                return channel.read()
            elif(frame == None):
                frame = channel.read()
            return func(frame, params)
        except (canlib.canNoMsg) as ex:
            return None
            pass
        except (canlib.canError) as ex:
            print(ex)

            
