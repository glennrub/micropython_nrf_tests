import os
from machine import SPI, Pin
from ssd1306 import SSD1306_SPI

mch = os.uname().machine
if 'PCA10028' in mch:
    scl = Pin.board.P15
    sda = Pin.board.P14
elif 'PCA10040' in mch:
    sck = Pin.board.P25
    miso = Pin.board.P24
    mosi = Pin.board.P23
    cs = Pin.board.P4
    dc = Pin.board.P28
    res = Pin.board.P29
elif 'PCA10056' in mch:
    sck = Pin.board.P47
    miso = Pin.board.P46
    mosi = Pin.board.P45
    cs = Pin.board.P4
    dc = Pin.board.P28
    res = Pin.board.P29
elif 'PCA10090' in mch:
    sck = Pin.board.P13
    miso = Pin.board.P12
    mosi = Pin.board.P11
    cs = Pin.board.P15
    dc = Pin.board.P16
    res = Pin.board.P17
else:
    raise Exception('Board not supported!')

spi = SPI(0, sck=sck, mosi=mosi, miso=miso)
print(spi)
disp_spi = SSD1306_SPI(128, 64, spi, dc, res, cs)
disp_spi.fill(0)
disp_spi.show()
disp_spi.text("Hello", 5, 5, 1)
disp_spi.text("World!", 5, 30, 1)
disp_spi.show()
print(len(disp_spi.buffer))
