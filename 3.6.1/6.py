import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 

def mapping(x, a, b): 
    return a * x + b 

x_list = list()
y_list = list()

t_0 = 6.9092



with  open('6.data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        y_list.append(list_line[2] / list_line[1])
        x_list.append(list_line[0] / 2)

x = np.array(x_list)
y = np.array(y_list)

x_aproc = x
y_aproc = y

args, covarian = curve_fit(mapping, x_aproc, y_aproc)
a, b = args[0], args[1]
y_fit = a * x_aproc + b

print(a)


fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs-')
plt.plot(x_aproc, y_fit, 'g')

plt.savefig("6.png")

with open("upd_data", "w+") as upd_data:
    for i in range(len(y)):
        strin = str(x[i]) + " " + str(y[i]) + "\n"
        upd_data.write(strin)


