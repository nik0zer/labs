import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

def mapping(x, a): 
    return a * x

l = list()
v = list()

with  open('data_6', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        v.append(list_line[0])
        l.append(list_line[1])

x = np.array(v)
y = np.array(l)

x1 = list()
y1 = list()

for i in range(len(l) -2):
    if(y[i] - y[len(l) - 1] != 0):
        x1.append(x[i] ** 2)
        y1.append((y[0] - y[len(l) - 1]) / (y[i] - y[len(l) - 1]))

x1.append(0)
y1.append(0)

x1 = np.array(x1)
y1 = np.array(y1)

x_aproc = np.array(x1)
y_aproc = np.array(y1)

args, covarian = curve_fit(mapping, x_aproc, y_aproc)
a = args[0]
y_fit = a * x_aproc

print(a)

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x1, y1, 'rs')
plt.plot(x_aproc, y_fit, 'g')

plt.savefig("4.png")
