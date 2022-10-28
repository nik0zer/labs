import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 

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


fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs')
#plt.plot(x_ful_aproc, y_fit, 'g')

plt.savefig("1.png")