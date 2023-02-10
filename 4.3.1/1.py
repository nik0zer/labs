import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math


num = list()
z = list()
with  open('data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        num.append(list_line[0])
        z.append(list_line[1])
        print("dsfd")

d1 = 350
d2 = 380
d1_list = list()
d2_list = list()
zm_2_list = list()
dzm_2_list = list()

for i in range(len(z)):
    zm_2 =  2 * math.sqrt(z[i] * num[i] * 5.46 * (10 ** -7) / 100) * 1000000
    zm_2_list.append(zm_2)
    dzm_2 = (0.2 / z[i]) / 2 * zm_2 * 2
    dzm_2_list.append(dzm_2)
    print(str(int(num[i])) + " " + str(zm_2) + " " + str(dzm_2))
    d1_list.append(d1)
    d2_list.append(d2)


fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(num, zm_2_list, 'rs')

plt.errorbar(num, zm_2_list, yerr = dzm_2_list, fmt = 'o', ls='none')

plt.plot(num, d1_list, 'bs-')
plt.plot(num, d2_list, 'gs-')
plt.savefig("1.png")
plt.show()
