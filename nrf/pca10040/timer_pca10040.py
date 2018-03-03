# Timer test for pca10028 - nrf51822, pca10040 - nrf52832, pca10056 - nrf52840

from machine import Timer
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
    num_of_timers = 5
else:
    raise Exception('Board not supported!')

# Test that all instances are available
for i in range(num_of_timers):
    tim = Timer(i, period=5000, mode=Timer.PERIODIC, callback=None)
    print(tim)
    tim.deinit()

# Test that too high instance number fails
try:
    tim = Timer(num_of_timers+1)
except ValueError:
    print('ValueError')

# Test that -1 is not allowed
try:
    tim = Timer(-1)
except ValueError:
    print("ValueError")

# Test that we can trigger one-shot callback
def oneshot_cb(timer):
    global num_of_callbacks
    global timer_obj
    num_of_callbacks += 1
    timer_obj = timer

num_of_callbacks = 0
timer_obj = None

tim = Timer(0, period=1000, mode=Timer.ONESHOT, callback=oneshot_cb)
print(tim)
tim.start()
time.sleep_ms(500)
tim.stop()

print(num_of_callbacks == 1)
print(timer_obj)

# Test that we can trigger periodic callback
def periodic_cb(timer):
    global num_of_callbacks
    global timer_obj
    num_of_callbacks += 1
    timer_obj = timer

num_of_callbacks = 0
timer_obj = None

tim = Timer(0, period=10000, mode=Timer.PERIODIC, callback=periodic_cb)
print(tim)
tim.start()
time.sleep_ms(100)
tim.stop()

print(num_of_callbacks >= 9 and num_of_callbacks <= 11)
print(timer_obj)
