# RTCounter multi test for pca10040 - nrf52832

from machine import RTCounter
import os
import time

mch = os.uname().machine
if 'PCA10040' in mch:
    pass
else:
    raise Exception('Board not supported!')

# Test that we can trigger two periodic callbacks in paralell
def periodic_cb0(counter):
    global num_of_callbacks0
    global counter_obj0
    num_of_callbacks0 += 1
    counter_obj0 = counter

def periodic_cb1(counter):
    global num_of_callbacks1
    global counter_obj1
    num_of_callbacks1 += 1
    counter_obj1 = counter

num_of_callbacks0 = 0
num_of_callbacks1 = 0
counter_obj0 = None
counter_obj1 = None

tim0 = RTCounter(2, period=1, mode=RTCounter.PERIODIC, callback=periodic_cb0)
tim1 = RTCounter(1, period=1, mode=RTCounter.PERIODIC, callback=periodic_cb1)

tim0.start()
tim1.start()
time.sleep_ms(1000)
tim0.stop()
tim1.stop()

print(num_of_callbacks0 > 7 and num_of_callbacks0 < 12)
print(num_of_callbacks1 > 7 and num_of_callbacks1 < 12)
print(counter_obj0)
print(counter_obj1)
