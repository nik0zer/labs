import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

def mapping(x, a, b):
    return a * x + b

x = list()
y = list()


with  open('data_1', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        x.append(list_line[0])
        y.append(list_line[1])


x_1 = np.array(x[4:8])
y_1 = np.array(y[4:8])
x = np.array(x)
y = np.array(y)

plt.figure(figsize=[8, 6])

plt.errorbar(x, y, xerr=0, yerr=0, fmt='b.')



args, covarian = scipy.optimize.curve_fit(mapping, x_1, y_1)
a, b = args[0], args[1]
teor_T = np.linspace(min(x), max(x), 1024)
teor_fermi = a * teor_T + b

plt.errorbar(teor_T, teor_fermi, xerr=0, yerr=0, fmt='g--')
perr = np.sqrt(np.diag(covarian))
print("a:", a, "Kp = ", a / np.pi / 2, "error_rate a:", perr[0], "b:", b, "error_rate b:", perr[1])

plt.show()

# a: 893.8600008328478 Kp =  142.26223756467343 error_rate a: 16.071628272807946 b: 0.9209998750729198 error_rate b: 0.98418224279982