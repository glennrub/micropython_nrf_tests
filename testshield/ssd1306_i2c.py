import os
from machine import I2C, Pin
from ssd1306_mod import SSD1306_I2C_Mod

mch = os.uname().machine
if 'PCA10028' in mch:
    scl = Pin.board.PA15
    sda = Pin.board.PA14
elif 'PCA10040' in mch:
    scl = Pin.board.PA3
    sda = Pin.board.PA4
elif 'PCA10056' in mch:
    pass
else:
    raise Exception('Board not supported!')

i2c = I2C(0, scl, sda)
print(i2c)
disp_i2c = SSD1306_I2C_Mod(128, 64, i2c)
disp_i2c.fill(1)
disp_i2c.show()
disp_i2c.text("Hello World!", 10, 10, 0)
disp_i2c.show()
print(len(disp_i2c.buffer))
