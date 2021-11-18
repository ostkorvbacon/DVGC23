def write(channel, func, frame):
    frame_fault = func(frame)
    channel.write(frame_fault)
