from cmath import tan
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

def mapping(x, a): 
    return a * x

v0 = 2251.6

e = list()
v = list()

e1 = list()
v1 = list()

fi = list()
pi = list()

#with  open('data_3', 'r')  as  data:
#    for line in data:
#        list_line = list((map(float, line.split())))
#        v.append(list_line[0])
#        e.append(list_line[1])

with  open('data_4', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        v.append(list_line[0])
        e.append(list_line[1])
        v1.append(list_line[0])
        e1.append(list_line[1])
        fi.append(list_line[2])
        pi.append(list_line[3])

x1 = list()
y1 = list()

for i in range(11):
    x1.append(math.sqrt(v1[i]))
    y1.append(math.tan(3.14 * fi[i] / pi[i] - 3.14 / 2))

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x1, y1, 'rs')

plt.savefig("6.png")