import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 

def mapping(x, a, b): 
    return a * x + b 

x_list = list()
y_list = list()
x1_list = list()
y1_list = list()

R = 5.4



with  open('1.data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        x_list.append(list_line[0])
        y_list.append(list_line[1] / 1000)
with  open('2.data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        x1_list.append(list_line[0])
        y1_list.append(list_line[1] / 1000)



for i in range(len(y_list)):
    x_list[i] = x_list[i] - y_list[i] * R * 1000
for i in range(len(y1_list)):
    x1_list[i] = x1_list[i] - y1_list[i] * R * 1000

x = np.array(x_list)
y = np.array(y_list)
x1 = np.array(x1_list)
y1 = np.array(y1_list)
print("a")
print(74 - 5.4 * 1000 / 1000 * 0.54)

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(x, y, 'rs')
plt.plot(x1, y1, 'gs')
#plt.plot(x_ful_aproc, y_fit, 'g')

plt.savefig("2.png")

with open("upd_data", "w+") as upd_data:
    for i in range(len(y)):
        strin = str(x[i]) + " " + str(y[i]) + "\n"
        upd_data.write(strin)


