_frame = None
_stored = 0

def set_stored(frame):
    global _stored
    global _frame
    if(_stored == 1):
        _stored = 0
        return _frame
    else:
        _frame = frame
        _stored = 1
        return None

def swap(frame, params = []):
    old_frame = set_stored(frame)
    if(old_frame is not None):
        return [frame, old_frame]
    else:
        return old_frame

if __name__ == '__main__':
    from canlib import canlib, Frame
    frame1 = Frame(
        id_=0,
        data=[0],
        flags=canlib.MessageFlag.EXT
    )
    frame2 = Frame(
        id_=1,
        data=[1],
        flags=canlib.MessageFlag.EXT
    )
    print(swap(frame1))
    print(swap(frame2))
    
