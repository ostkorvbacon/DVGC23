from canlib import Frame

def print_frame(frame):
    print("id_ = {}".format(frame.id))
    print("data = \\x", end = "")
    print('\\x'.join('{:02x}'.format(d) for d in frame.data))
    print("flags = {}\n".format(frame.flags))
