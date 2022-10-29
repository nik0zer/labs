import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

def mapping(x, a, b): 
    return a * x + b 

v0 = 2251.6
e0 = 0.0191

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
v1 = list()
for i in range(len(v)):
    v1.append(math.log((v[i]/v[0])))
v1 = np.array(v1)

print(math.log((v0/v[0])))

he = list()

for i in range(len(v)):
    he.append(e[i]/e0)

he = np.array(he)

v = np.array(v)

ht1 = list()
ht2 = list()

h = 1.5 * 10 ** -3
a = 45 * 10 ** -3 /2
s1 = 5.2 * 10 ** 7
s2 = 3.96 * 10 ** 7
u0 = 4 * 3.14 * 10 ** -7
for i in range(len(v)):
    ht1.append(1 / (math.sqrt(1 + 1 / 4 * ((a * h * s1 * u0 * v[i] *2 *3.14) ** 2))))
for i in range(len(v)):
    ht2.append(1 / (math.sqrt(1 + 1 / 4 * ((a * h * s2 * u0 * v[i] *2 *3.14) ** 2))))

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)
plt.plot(v1, he, 'rs')
plt.plot(v1, ht1, 'gs')
plt.plot(v1, ht2, 'bs')
plt.savefig("5.png")