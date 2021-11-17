# for testing purpouses
def do_nothing(frame):
    return frame

def write(channel, func, frame):
    frame_fault = func(frame)
    channel.write(frame_fault)
