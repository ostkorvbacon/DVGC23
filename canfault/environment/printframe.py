from canlib import Frame

"""Print a frame formatted for easy reading"""
def print_frame(frame):
    if not isinstance(frame, Frame):
        raise TypeError("print_frame requires type Frame")
    else:
        print("id_ = {}".format(frame.id))
        print("data = \\x", end = "")
        print('\\x'.join('{:02x}'.format(d) for d in frame.data))
        print("flags = {}\n".format(frame.flags))
