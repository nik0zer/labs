import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math


f = list()
a = list()
f1 = list()
a1 = list()
with  open('data_2', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        f.append(list_line[0])
        a.append(list_line[1])

for i in range(0, 50000):
    f1.append(i)
    a1.append(77)
        
plt.plot(f, a, 'b--')
plt.plot(f1, a1, '--')

plt.savefig("1.png")
plt.show()