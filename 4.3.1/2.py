import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math


def mapping(x, a, b): 
    return a * x+ b

m = list()
Xm = list()
with  open('data1', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        m.append(list_line[0])
        Xm.append(list_line[1])

m1 = np.array(m)

y = np.array(Xm)
x = np.array(m)

x_aproc = x
y_aproc = y

args, covarian = curve_fit(mapping, m, Xm)
a, b = args[0], args[1]
y_fit = a * m1 + b

print("a " + str(args[0]))


sum = 0
length = len(x_aproc)
for i in range(len(x_aproc)):
    sum += (y_fit[i] - y_aproc[i]) ** 2
error_rate = math.sqrt(sum / (length + 1))
#print(error_rate)

x_sr = 0
y_sr = 0

x_dr = 0
y_dr = 0

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

error_rate_a = math.sqrt(((y_dr / x_dr) - a ** 2) / (length - 2))
print("error_rate_a" + " " + str(error_rate_a))

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(m, Xm, 'bs')
plt.plot(m1, y_fit, 'g-')

plt.errorbar(m, Xm, yerr = 0.05, fmt = 'o', ls='none')

plt.savefig("2.png")
plt.show()
