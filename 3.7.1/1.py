import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

def mapping(x, a, b): 
    return a * x + b 

v0 = 2251.6

e = list()
v = list()

e1 = list()
v1 = list()

fi = list()
pi = list()

with  open('data_3', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        v.append(list_line[0])
        e.append(list_line[1])

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

for i in range(len(e)):
    if v[i] >= v0 * 0.2:
        break
    x1.append(v[i] ** 2)
    y1.append(1 / (e[i] ** 2))

y = np.array(y1)
x = np.array(x1)

x_aproc = x
y_aproc = y

args, covarian = curve_fit(mapping, x_aproc, y_aproc)
a, b = args[0], args[1]
y_fit = a * x_aproc + b


sum = 0
length = len(x_aproc)
for i in range(len(x_aproc)):
    sum += (y_fit[i] - y_aproc[i]) ** 2
error_rate = math.sqrt(sum / (length + 1))
print(error_rate)

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

print(error_rate_a)

x_sr_2 = 0
for i in range(length):
    x_sr_2 += x_aproc[i] ** 2
x_sr_2 /= length

error_rate_b = error_rate_a * math.sqrt(x_sr_2)
print(error_rate_b) 

print(error_rate_a / a)
print(error_rate_b / b)

y_fit = np.append(y_fit, 0)
x_aproc = np.append(x_aproc, -b/a)

print(b)
print(a)



fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs')
plt.plot(x_aproc, y_fit, 'g')

plt.savefig("1.png")