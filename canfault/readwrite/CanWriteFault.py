from canlib import canlib
import asyncio
import constants

# for testing purpouses
def do_nothing(frame):
    return frame

def write(channel, func, frame):
    try:
        frame_fault = func(frame)
        channel.write(frame_fault)
    except (canlib.canNoMsg) as ex:
        pass
    except (canlib.canError) as ex:
        print(ex)
