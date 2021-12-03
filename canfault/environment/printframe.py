from canlib import Frame

def print_frame(frame):
    """Prints a Frame formatted for easy reading"""
    if not isinstance(frame, Frame):
        raise TypeError("print_frame requires type Frame")
    else:
        print("id_ = {}".format(hex(frame.id)))
        print("data = \\x", end = "")
        print('\\x'.join('{:02x}'.format(d) for d in frame.data))
        print("flags = {}\n".format(frame.flags))
