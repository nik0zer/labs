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

for i in range(len(v1)):
    x1.append(math.sqrt(v1[i]))
    y1.append((3.14 * fi[i] / pi[i] - 3.14 / 2) - 3.14/4)

y = np.array(y1)
x = np.array(x1)

x_aproc = list()
y_aproc = list()

for i in range(17, 24):
    x_aproc.append(x[i])
    y_aproc.append(y[i])

x_aproc.append(0)
y_aproc.append(0)

x_aproc = np.array(x_aproc)
y_aproc = np.array(y_aproc)

args, covarian = curve_fit(mapping, x_aproc, y_aproc)
a = args[0]
y_fit = a * x_aproc

x_sr = 0
y_sr = 0

x_dr = 0
y_dr = 0

length = len(x_aproc)

for i in range(length):
    x_sr += x_aproc[i]
x_sr /= length

for i in range(length):
    x_dr += (x_aproc[i] - x_sr) ** 2
x_dr /= length

for i in range(length):
    y_sr += y_aproc[i]
y_sr /= length

for i in range(length):
    y_dr += (y_aproc[i] - y_sr) ** 2
y_dr /= length


error_rate_a = math.sqrt((1.05 * (y_dr / x_dr) - a**2) / (length -  3))

print(error_rate_a)


print(error_rate_a / a)

print(a)



fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs')
plt.plot(x_aproc, y_fit, 'g')

plt.savefig("2.png")