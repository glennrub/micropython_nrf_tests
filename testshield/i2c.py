import os
from machine import I2C, Pin

mch = os.uname().machine
if 'PCA10028' in mch:
    scl = Pin.board.P5
    sda = Pin.board.P6
elif 'PCA10040' in mch:
    scl = Pin.board.P30
    sda = Pin.board.P31
elif 'PCA10056' in mch:
    scl = Pin.board.P30
    sda = Pin.board.P31
elif 'PCA10090' in mch:
    print("SKIP") # nrf9160 can never scan()
else:
    raise Exception('Board not supported!')

i = I2C(0, scl, sda)
res = i.scan()
print(res)
