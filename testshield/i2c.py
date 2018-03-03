import os
from machine import I2C, Pin

mch = os.uname().machine
if 'PCA10028' in mch:
    scl = Pin.board.PA28
    sda = Pin.board.PA25
elif 'PCA10040' in mch:
    scl = Pin.board.PA24
    sda = Pin.board.PA23
elif 'PCA10056' in mch:
    pass
else:
    raise Exception('Board not supported!')

i = I2C(0, scl, sda)
res = i.scan()
print(res)
