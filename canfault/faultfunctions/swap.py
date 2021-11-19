_frame = None
_stored = 0

def set_stored(frame):
    if(_stored == 1):
        _stored = 0
        return _frame
    else:
        _frame = frame
        _stored = 1
        return None

def swap(frame, params = []):
    if(set_stored is None):
        return set_stored(frame)
    else:
        return [set_stored(frame), frame]