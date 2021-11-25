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

    
