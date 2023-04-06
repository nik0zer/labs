import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math


D = list()
d = list()
with  open('data.txt', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        D.append(1 / list_line[0])
        d.append(list_line[1])




fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(D, d, 'gs-')
plt.savefig("1.png")
plt.show()
