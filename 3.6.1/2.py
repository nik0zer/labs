import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 

def mapping(x, a, b): 
    return a * x + b 

x_list = list()
y_list = list()

t_0 = 6.9092


i = 1
with  open('2.data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        y_list.append(list_line[0])
        x_list.append(i * 1000)
        i += 1

x = np.array(x_list)
y = np.array(y_list)


fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs-')
#plt.plot(x_ful_aproc, y_fit, 'g')

plt.savefig("2.png")

with open("upd_data", "w+") as upd_data:
    for i in range(len(y)):
        strin = str(x[i]) + " " + str(y[i]) + "\n"
        upd_data.write(strin)


