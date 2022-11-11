import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

u = list()
i = list()
r = list()

b = list()
ib = list()


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
        

u1 = list()
i1 = list()
r1 = list()

j = 1
with  open('U(I)_plane1', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        u1.append(list_line[0])
        i1.append(list_line[1])

u2 = list()
i2 = list()
r2 = list()

j = 1
with  open('U(I)_plane2', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        u2.append(list_line[0])
        i2.append(list_line[1])

r.append(u[0] / 23.5)
r1.append(u1[0] / 10)
r2.append(u2[0] / 10)

for j in range(1, len(u)):
    r.append(u[j] / 23.5)


for j in range(1, len(u)):
    r1.append(u1[j] / 10)

for j in range(1, len(u)):
    r2.append(u2[j] / 10)

y = np.array(r)
x = np.array(b)
x = x ** 2
x = x / 1000
y *= 100

y1 = np.array(r1)
x1 = np.array(b)
x1 = x1 ** 2
x1 = x1 / 1000
y1 *= 100

y2 = np.array(r2)
x2 = np.array(b)
x2 = x2 ** 2
x2 = x2 / 1000
y2 *= 100


fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs--')
plt.plot(x1, y1, 'gs--')
plt.plot(x2, y2, 'bs--')

plt.savefig("2.png")


