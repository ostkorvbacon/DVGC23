def write(channel, func, frame, params = []):
    frame_fault = func(frame, params)
    if(frame_fault != None):
        channel.write(frame_fault)
