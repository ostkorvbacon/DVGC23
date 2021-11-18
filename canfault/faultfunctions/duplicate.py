from canlib import canlib, Frame
from environment import transciever

def duplicate(frame, params = []):
    return [frame,frame]


if __name__ == '__main__':
    fr = transciever.framefactory.random()
    print(duplicate(fr))