# RTCounter test for pca10040 - nrf52832

from machine import RTCounter
import os
import time

try:
    import ble
    ble_enabled = True
except:
    ble_enabled = False

if ble_enabled:
    print("SKIP")
    raise SystemExit

mch = os.uname().machine
if 'PCA10040' in mch:
    num_of_counters = 3
else:
    raise Exception('Board not supported!')

# Test that all instances are available
for i in range(num_of_counters):
    tim = RTCounter(i, period=5, mode=RTCounter.PERIODIC, callback=None)
    print(tim)
    tim.deinit()

# Test that too high instance number fails
try:
    tim = RTCounter(num_of_counters+1)
except ValueError:
    print('ValueError')

# Test that -1 is not allowed
try:
    tim = RTCounter(-1)
except ValueError:
    print("ValueError")

# Test that we can trigger one-shot callback
def oneshot_cb(counter):
    global num_of_callbacks
    global counter_obj
    num_of_callbacks += 1
    counter_obj = counter

num_of_callbacks = 0
counter_obj = None

tim = RTCounter(1, period=10, mode=RTCounter.ONESHOT, callback=oneshot_cb)
print(tim)
tim.start()
time.sleep_ms(5000)
tim.stop()

print(num_of_callbacks == 1)
print(counter_obj)

# Test that we can trigger periodic callback
def periodic_cb(counter):
    global num_of_callbacks
    global counter_obj
    num_of_callbacks += 1
    counter_obj = counter

num_of_callbacks = 0
counter_obj = None

tim = RTCounter(1, period=1, mode=RTCounter.PERIODIC, callback=periodic_cb)
print(tim)
tim.start()
time.sleep_ms(1000)
tim.stop()

print(num_of_callbacks >= 7 and num_of_callbacks < 12)
print(counter_obj)
