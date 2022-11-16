import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

u = list()
i = list()
r = list()

b = list()
ib = list()

def mapping(x, a, b): 
    return a * x + b 

with  open('B(I)_data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        b.append(list_line[0])
        ib.append(list_line[1])

j = 1
with  open('U(I)_cir', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        u.append(list_line[0])
        i.append(list_line[1])


r.append(u[0] / 23.5)

for j in range(1, len(u)):
    r.append(u[j] / 23.5)

y = np.array(r)
x = np.array(b)
x = x ** 2
x = x / 1000
y *= 100


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


print(a)
print(b)


fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs--')
plt.plot(x_aproc, y_fit, 'g-')
plt.savefig("korb.png")