import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

def mapping(x, a, b):
    return a * x + b

T = list()
fermi = list()


with  open('data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        T.append(list_line[0])
        fermi.append(list_line[1])


plt.figure(figsize=[20, 10])
plt.errorbar(T, fermi, xerr=0, yerr=0, fmt='b.')

T_line = T[8:len(T) - 10]
fermi_line = fermi[8:len(T) - 10]



args, covarian = scipy.optimize.curve_fit(mapping, T_line, fermi_line)
a, b = args[0], args[1]
teor_T = np.linspace(min(T_line), max(T_line), 1024)
teor_fermi = a * teor_T + b

plt.errorbar(teor_T, teor_fermi, xerr=0, yerr=0, fmt='g--')
perr = np.sqrt(np.diag(covarian))
print("a:", a, "error_rate a:", perr[0], "b:", b, "error_rate b:", perr[1])

plt.show()