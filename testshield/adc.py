import os
from machine import ADC

mch = os.uname().machine
if 'PCA10028' in mch:
    pass
elif 'PCA10040' in mch:
    vdd = 2833 # 2.833v
    adc_num = 1 # P0.03
    min_voltage = 1380 # 1.38v
    max_voltage = 1420 # 1.42v
elif 'PCA10056' in mch:
    pass
elif 'PCA10090' in mch:
    pass
else:
    raise Exception('Board not supported!')

a = ADC(adc_num)

scaler = 1000
num_samples = 100
max_adc_val = 255

val = 0
for i in range(0, num_samples):
    val += a.value()
temp_res = val * scaler
res = vdd * temp_res // (num_samples * scaler) // max_adc_val

print(res >= min_voltage and res <= max_voltage) 
