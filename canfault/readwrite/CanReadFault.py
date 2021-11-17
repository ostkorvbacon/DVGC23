from canlib import canlib

def read(channel, func):
    while True:
        try:
            frame = channel.read()
            return func(frame)
            break
        except (canlib.canNoMsg) as ex:
            pass
        except (canlib.canError) as ex:
            print(ex)
