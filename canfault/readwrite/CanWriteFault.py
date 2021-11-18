def write(channel, func, frame, params = []):
    frame_fault = func(frame, params)
    if(frame_fault is not None):
        if(isinstance(frame_fault, list)):
            for single_frame in frame_fault:
                channel.write(single_frame)
        else:
            channel.write(frame_fault)
