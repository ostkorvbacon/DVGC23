from canlib import canlib

# Used to read from the bus if no frame is supplied.
# Used to pretend to read a frame from the bus if a frame is supplied.
# May be used when you want to inject faults in only one of the components
# connected to a bus with multiple components connected to it.
def read(channel, func, frame = None):
    while True:
        try:
            if(frame is None):
                frame = channel.read()
            return func(frame)
            break
        except (canlib.canNoMsg) as ex:
            pass
        except (canlib.canError) as ex:
            print(ex)
