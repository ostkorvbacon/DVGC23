def write(channel, func, frame, params = []):
    frame_fault = func(frame, params)
    channel.write(frame_fault)
