import os
from machine import SPI, Pin
from ssd1306 import SSD1306_SPI

mch = os.uname().machine
if 'PCA10028' in mch:
    scl = Pin.board.PA15
    sda = Pin.board.PA14
elif 'PCA10040' in mch:
    sck = Pin.board.PA24
    mosi = Pin.board.PA23
    miso = Pin.board.PA25
    dc = Pin.board.PA22
    res = Pin.board.PA20
    cs = Pin.board.PA19
elif 'PCA10056' in mch:
    pass
else:
    raise Exception('Board not supported!')

spi = SPI(1, sck=sck, mosi=mosi, miso=miso)
print(spi)
disp_spi = SSD1306_SPI(128, 64, spi, dc, res, cs)
disp_spi.fill(1)
disp_spi.show()
disp_spi.text("Hello World!", 10, 10, 0)
disp_spi.show()
print(len(disp_spi.buffer))
