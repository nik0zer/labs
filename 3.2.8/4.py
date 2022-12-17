import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import math

def mapping(x, a, b): 
    return a * x + b 

x_list = list()
y_list = list()

U2 = 96.5
U1 = 71.6
C = 50 / (10 ** 9)

K_teor = math.log((116.4 - U1)/(116.4 - U2))


with  open('4.data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        x_list.append(list_line[0] * (10 ** 3))
        y_list.append(1 / list_line[1])

x = np.array(x_list)
y = np.array(y_list)


y1_list = list()

for i in range(len(x_list)):
    y1_list.append(x_list[i] * C * K_teor)
y1 = np.array(y1_list)

x_aproc = x
y_aproc = y

args, covarian = curve_fit(mapping, x_aproc, y_aproc)
a, b = args[0], args[1]
y_fit = a * x_aproc + b

print(a)

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs')
plt.plot(x, y1, 'gs-')
plt.plot(x_aproc, y_fit, 'r--')

plt.savefig("4.png")

with open("upd_data", "w+") as upd_data:
    for i in range(len(y)):
        strin = str(x[i]) + " " + str(y[i]) + "\n"
        upd_data.write(strin)


