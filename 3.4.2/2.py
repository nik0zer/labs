import math
from pyexpat.errors import XML_ERROR_SUSPEND_PE
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 

def mapping(x, a, b): 
    return a * x + b 

T_list = []
U_list = []
t_list = []

t_0 = 6.9092



with  open('data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        T_list.append(list_line[0])
        U_list.append(list_line[1])
        t_list.append(list_line[2])

for i in range(len(T_list)):
    T_list[i] = T_list[i] + U_list[i] * 24

x = np.array(T_list)
y_list = []

for i in range(len(t_list)):
    y_list.append(1 / ((float)(t_list[i] ** 2 - t_0 ** 2)))

y = np.array(y_list)

correction = y[0]

y = y - correction



x_aproc = x[4:len(x)-4]
y_aproc = y[4:len(y)-4]
x_ful_aproc = x[4:len(x)]

args, covarian = curve_fit(mapping, x_aproc, y_aproc)
a, b = args[0], args[1]
y_fit = a * x_ful_aproc + b
y_fit = np.append(y_fit, 0)
x_ful_aproc = np.append(x_ful_aproc, -b/a)
print(-b/a)

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

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs')
plt.plot(x_ful_aproc, y_fit, 'g')

plt.savefig("2.png")

with open("upd_data", "w+") as upd_data:
    for i in range(len(y)):
        strin = str(x[i]) + " " + str(y[i]) + "\n"
        upd_data.write(strin)


