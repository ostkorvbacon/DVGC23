from canlib import canlib, Frame, frame 
import time
'''Skickar arrayer med parameter, kallar på funktionen'''
def delay(frame, params =[]): 
    time.sleep(params[0])
    return frame