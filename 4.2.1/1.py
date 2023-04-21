import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

def mapping(x, a, b): 
    return a * x + b

nm = list()
d = list()



with  open('data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        nm.append(list_line[0])
        d.append((list_line[2] - list_line[1] + 0.21) * 0.09)

d1 = list()
d2 = list()
m1 = list()
m2 = list()

for i in range(len(nm)):
    if nm[i] % 2 == 0:
        m2.append(nm[i] / 2)
        d2.append(d[i])
    else:
        m1.append((nm[i] - 1) / 2)
        d1.append(d[i])

d1 = (np.array(d1) / 2) ** 2
d2 = (np.array(d2) / 2) ** 2
m1 = np.array(m1)
m2 = np.array(m2)

args, covarian = curve_fit(mapping, m1, d1)
a_1, b_1 = args[0], args[1]
y_fit_1 = a_1 * m1 + b_1

print(a_1)

args, covarian = curve_fit(mapping, m2, d2)
a_2, b_2 = args[0], args[1]
y_fit_2 = a_2 * m2 + b_2

print(a_2)





def err_rate(x_aproc, y_fit, y_aproc, a):
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


err_rate(m1, y_fit_1, d1, a_1)
err_rate(m2, y_fit_2, d2, a_2)


plt.plot(m1, d1, 'bs')
plt.plot(m2, d2, 'gs')
plt.plot(m1, y_fit_1, 'b')
plt.plot(m2, y_fit_2, 'g')
plt.savefig("1.png")
plt.show()









