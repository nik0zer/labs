import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math


def mapping(x, a, b): 
    return a * x+ b

xm_1 = list()
xm_2 = list()
xm_3 = list()
xm_4 = list()
m_1 = list()
m_2 = list()
m_3 = list()
m_4 = list()
i = 1
with  open('data_1_1', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        xm_1.append(list_line[0])
        m_1.append(i)
        i += 1
i = 1
with  open('data_1_2', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        xm_2.append(list_line[0])
        m_2.append(i)
        i += 1
i = 1
with  open('data_1_3', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        xm_3.append(list_line[0])
        m_3.append(i)
        i += 1
i = 1
with  open('data_1_4', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        xm_4.append(list_line[0])
        m_4.append(i)
        i += 1
i = 1

vint = 4



xm_1 = np.array(xm_1) * 4
xm_2 = np.array(xm_2) * 4
xm_3 = np.array(xm_3) * 4
xm_4 = np.array(xm_4) * 4

m_1 = np.array(m_1)
m_2 = np.array(m_2)
m_3 = np.array(m_3)
m_4 = np.array(m_4)

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)



y = np.array(xm_1)
x = np.array(m_1)

x_aproc = x
y_aproc = y

args, covarian = curve_fit(mapping, m_1, xm_1)
a, b = args[0], args[1]
y_fit = a * m_1 + b

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

error_rate_a = math.sqrt(((y_dr / x_dr) - a ** 2) / (length - 2))
print("error_rate_a" + " " + str(error_rate_a))


plt.plot(m_1, y_fit, 'b--')






y = np.array(xm_2)
x = np.array(m_2)

x_aproc = x
y_aproc = y

args, covarian = curve_fit(mapping, m_2, xm_2)
a, b = args[0], args[1]
y_fit = a * m_2 + b

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

error_rate_a = math.sqrt(((y_dr / x_dr) - a ** 2) / (length - 2))
print("error_rate_a" + " " + str(error_rate_a))

plt.plot(m_2, y_fit, 'g--')






y = np.array(xm_3)
x = np.array(m_3)

x_aproc = x
y_aproc = y

args, covarian = curve_fit(mapping, m_3, xm_3)
a, b = args[0], args[1]
y_fit = a * m_3 + b

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

error_rate_a = math.sqrt(((y_dr / x_dr) - a ** 2) / (length - 2))
print("error_rate_a" + " " + str(error_rate_a))

plt.plot(m_3, y_fit, 'c--')





y = np.array(xm_4)
x = np.array(m_4)

x_aproc = x
y_aproc = y

args, covarian = curve_fit(mapping, m_4, xm_4)
a, b = args[0], args[1]
y_fit = a * m_4 + b

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

error_rate_a = math.sqrt(((y_dr / x_dr) - a ** 2) / (length - 2))
print("error_rate_a" + " " + str(error_rate_a))




plt.plot(m_4, y_fit, 'm--')






plt.plot(m_1, xm_1, 'bs')
plt.plot(m_2, xm_2, 'gs')
plt.plot(m_3, xm_3, 'cs')
plt.plot(m_4, xm_4, 'ms')
plt.savefig("1.png")
plt.show()
