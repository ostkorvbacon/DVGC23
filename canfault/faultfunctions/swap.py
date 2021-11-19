_frame = None
_stored = 0

def set_stored(frame):
    global _stored
    global _frame
    if(_stored == 1):
        _stored = 0
        ret = _frame
        _frame = None
        return ret, 1
    else:
        _frame = frame
        _stored = 1
        return None, 0

def swap(frame, params = []):
    old_frame, stored = set_stored(frame)
    if(stored == 1):
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
    
