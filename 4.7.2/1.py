import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

def mapping(x, a, b): 
    return a * x + b

d = list()
m = list()


with  open('data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        m.append(list_line[0])
        d.append(list_line[1])

d = np.array(d)
m = np.array(m)

r = d / 2

r_2 = r ** 2

args, covarian = curve_fit(mapping, m, r_2)
a, b = args[0], args[1]
y_fit = a * m + b

print("a " + str(args[0]))

x_aproc = m
y_aproc = r_2


sum = 0
length = len(x_aproc)
for i in range(len(x_aproc)):
    sum += (y_fit[i] - y_aproc[i]) ** 2
error_rate = math.sqrt(sum / (length + 1))

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

y_err = (0.1 / r) * 2 * r_2

plt.errorbar(m, r_2, yerr = y_err, fmt = 'o', ls='none')

plt.plot(m, r_2, 'b.')
plt.plot(m, y_fit, '--')
plt.savefig("1.png")
plt.show()