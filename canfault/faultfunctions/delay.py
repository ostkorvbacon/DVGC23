import time
from canlib import canlib, Frame
# Mera from, kanske env eller canlib? Import?
def delay(frame, delay = 0): 
    time.sleep(1)
    return frame

#CONNECTION_DELAY = 5 
#Overload är gammalt ? Finns det något nyare?