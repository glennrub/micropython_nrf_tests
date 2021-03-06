import os
from machine import SPI, Pin
from sdcard import SDCard

mch = os.uname().machine
if 'PCA10028' in mch:
    sck = Pin.board.P29
    miso = Pin.board.P28
    mosi = Pin.board.P25
    cs = Pin.board.P16
elif 'PCA10040' in mch:
    sck = Pin.board.P25
    miso = Pin.board.P24
    mosi = Pin.board.P23
    cs = Pin.board.P15
elif 'PCA10056' in mch:
    sck = Pin.board.P47
    mosi = Pin.board.P45
    miso = Pin.board.P46
    cs = Pin.board.P37 # P1.05
elif 'PCA10090' in mch:
    sck = Pin.board.P13
    miso = Pin.board.P12
    mosi = Pin.board.P11
    cs = Pin.board.P4
else:
    raise Exception('Board not supported!')

spi = SPI(1, sck=sck, mosi=mosi, miso=miso)
sd = SDCard(spi, cs)

os.mount(sd, '/')
print('testfile.txt' in os.listdir())
print([open("testfile.txt", "r").read()])
