import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

l = list()
v = list()

with  open('data_6', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        v.append(list_line[0])
        l.append(list_line[1])

x = np.array(v)
y = np.array(l)

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs')

plt.savefig("3.png")
