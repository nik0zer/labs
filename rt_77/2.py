import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math


f = list()
a = list()
f1 = list()
a1 = list()
with  open('data_1', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        f.append(list_line[0])
        a.append(20 * math.log10(list_line[1]))

for i in range(50, 50000):
    f1.append(i)
    a1.append(20 * math.log10(40400) - 3)
        
plt.plot(f, a, 'bs-')
plt.plot(f1, a1, '--')

plt.savefig("2.png")
plt.show()