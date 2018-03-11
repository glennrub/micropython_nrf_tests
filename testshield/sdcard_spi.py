import os
from machine import SPI, Pin
from sdcard import SDCard

mch = os.uname().machine
if 'PCA10028' in mch:
    sck = Pin.board.PA4
    mosi = Pin.board.PA5
    miso = Pin.board.PA6
    cs = Pin.board.PA14
elif 'PCA10040' in mch:
    sck = Pin.board.PA29
    mosi = Pin.board.PA30
    miso = Pin.board.PA31
    cs = Pin.board.PA13
elif 'PCA10056' in mch:
    pass
else:
    raise Exception('Board not supported!')

spi = SPI(0, sck=sck, mosi=mosi, miso=miso)
sd = SDCard(spi, cs)

os.mount(sd, '/')
print('testfile.txt' in os.listdir())
print([open("testfile.txt", "r").read()])
