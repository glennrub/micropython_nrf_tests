import os
from machine import I2C, Pin
from ssd1306_mod import SSD1306_I2C_Mod

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
    scl = Pin.board.P18
    sda = Pin.board.P19
else:
    raise Exception('Board not supported!')

i2c = I2C(1, scl, sda)
print(i2c)
disp_i2c = SSD1306_I2C_Mod(128, 64, i2c)
disp_i2c.fill(1)
#disp_i2c.show()
disp_i2c.text("Hello World!", 5, 5, 0)
disp_i2c.show()
print(len(disp_i2c.buffer))
