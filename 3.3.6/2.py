import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

u = list()
i = list()

with  open('U(I)_cir', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        u.append(list_line[0])
        i.append(list_line[1])

u1 = list()
i1 = list()

with  open('U(I)_plane1', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        u1.append(list_line[0])
        i1.append(list_line[1])

u2 = list()
i2 = list()

with  open('U(I)_plane2', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        u2.append(list_line[0])
        i2.append(list_line[1])

y = np.array(u)
x = np.array(i)

y1 = np.array(u1)
x1 = np.array(i1)

y2 = np.array(u2)
x2 = np.array(i2)


fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs--')
plt.plot(x1, y1, 'gs--')
plt.plot(x2, y2, 'bs--')

plt.savefig("2.png")


