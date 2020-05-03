import os, time
from machine import PWM, Pin

mch = os.uname().machine
if 'PCA10040' in mch:
    pin = Pin.board.P14
elif 'PCA10056' in mch:
    pin = Pin.board.P36 # P1.04
elif 'PCA10090' in mch:
    pin = Pin.board.P3
else:
    raise Exception('Board not supported!')

# center
p = PWM(0, pin, freq=PWM.FREQ_125KHZ, pulse_width=188, period=2500, mode=PWM.MODE_HIGH_LOW)
p.init()
time.sleep_ms(200)
p.deinit()

time.sleep_ms(200)

# left 
p = PWM(0, pin, freq=PWM.FREQ_125KHZ, pulse_width=105, period=2500, mode=PWM.MODE_HIGH_LOW)
p.init()
time.sleep_ms(200)
p.deinit()

time.sleep_ms(200)

# right
p = PWM(0, pin, freq=PWM.FREQ_125KHZ, pulse_width=275, period=2500, mode=PWM.MODE_HIGH_LOW)
p.init()
time.sleep_ms(200)
p.deinit()

print(p)
