import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math


f = list()
a = list()
f_1 = list()
a_1 = list()
f1 = list()
a1 = list()
with  open('data_1', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        f.append(list_line[0])
        a.append(20 * math.log10(list_line[1]))

with  open('data_2', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        f_1.append(list_line[0])
        a_1.append(20 * math.log10(list_line[1]))


plt.plot(f, a, 'bs-')
plt.plot(f_1, a_1, 'rs-')

plt.savefig("1.png")
plt.show()