import matplotlib.pyplot as plt
import numpy as np
import scipy
import math

def mapping(x, a, b):
    return a * x + b

f = list()
a = list()
with  open('data_1', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        f.append(list_line[0])
        a.append(list_line[1])
        
plt.plot(np.log10(f), 20 * np.log10(a), 'b.')

args, covarian = scipy.optimize.curve_fit(mapping, np.log10(f[3:]), 20 * np.log10(a[3:]))
a_1, b_1 = args[0], args[1]

plt.plot(np.log10(f), np.log10(f) * a_1 + b_1, 'g--')
print("db(0)", 20 * np.log10(a[0]))
print("db = -3", ((20 * np.log10(a[0]) - 3) - b_1) / a_1)
print("db = 0", (0 - b_1) / a_1)
print("db/dec", a_1)

plt.savefig("1.png")
plt.show()