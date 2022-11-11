import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

b = list()
i = list()

with  open('B(I)_data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        b.append(list_line[0])
        i.append(list_line[1])


y = np.array(b)
x = np.array(i)


fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs--')

plt.savefig("1.png")