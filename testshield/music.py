import os, music
from machine import Pin

mch = os.uname().machine
if 'PCA10028' in mch:
    pass
elif 'PCA10040' in mch:
    pin_str = "P13"
elif 'PCA10056' in mch:
    pin_str = "P35" # P1.03
else:
    raise Exception('Board not supported!')

p = Pin(pin_str, mode=Pin.OUT)
music.play(music.PRELUDE, pin=p)

print(res)
