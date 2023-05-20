import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from scipy.optimize import curve_fit 
import math


b = list()
h1 = list()
h2 = list()
h3 = list()
h4 = list()


with  open('data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        b.append(list_line[0])
        h1.append(list_line[1])
        h2.append(list_line[2])
        h3.append(list_line[3])
        h4.append(list_line[4])


b = np.array(b)
#b = b / 180 * math.pi


h1 = np.array(h1)
h2 = np.array(h2)
h3 = np.array(h3)
h4 = np.array(h4)

d = h2 ** 2 / h1 ** 2

y = (h4 - h3) / (h4 + h3) * ((2 * np.sqrt(d)) / (1 + d))
print(y)
print(b) 

b1 = list()
for i in range(91) : 
    b1.append(i)

b1 = np.array(b1)





plt.plot(b, y, 'g*')
plt.savefig("1.png")
plt.show()