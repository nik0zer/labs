import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

I_13 = list()
I_14 = list()
I_15 = list()
I_16 = list()
U = list()

def mapping(x, a, b): 
    return a * x + b 

with  open('1.3A', 'r')  as  data:
    for line in data:
        list_line = list(map(float, line.split()))
        U.append(list_line[0])
        I_13.append(list_line[1])

with  open('1.4A', 'r')  as  data:
    for line in data:
        list_line = list(map(float, line.split()))
        I_14.append(list_line[0])

with  open('1.5A', 'r')  as  data:
    for line in data:
        list_line = list(map(float, line.split()))
        I_15.append(list_line[0])

with  open('1.6A', 'r')  as  data:
    for line in data:
        list_line = list(map(float, line.split()))
        I_16.append(list_line[0])

y = np.array(I_15)
x = np.array(U)
x = x**(3/2)



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
plt.savefig("3.png")