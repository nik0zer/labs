import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

def mapping(x, a, b): 
    return a * x

v = list()
l = list()
err_l = list()
err_v = list()

with  open('data_2', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        v.append(list_line[0])
        l.append(list_line[1])
        err_l.append(list_line[2])
        err_v.append(list_line[3])


fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

v = np.array(v)
err_l = np.array(err_l)
l = np.array(l)
err_v = np.array(err_v)

v = 1 / v

plt.errorbar(v, l, yerr = err_l, xerr= err_v, fmt = 'o', ls='none')

plt.plot(v, l, 'bs')



y = np.array(l)
x = np.array(v)

x_aproc = x
y_aproc = y

args, covarian = curve_fit(mapping, v, l)
a = args[0]
y_fit = a * v

print("a " + str(args[0]))


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

#error_rate_a = math.sqrt(((y_dr / x_dr) - a ** 2) / (length - 2))
#print("error_rate_a" + " " + str(error_rate_a))


plt.plot(v, y_fit, 'b--')
print(y_fit[2] / v[2])

plt.savefig("2.png")
plt.show()