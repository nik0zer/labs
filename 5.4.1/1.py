import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

def mapping(x, a, b):
    return a * x + b

P = list()
I = list()


with  open('data_1', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        P.append(100 - list_line[0] / 10)
        I.append(list_line[1])


p_vverh = P[:24]
I_vverh = I[:24]

p_niz = P[24:]
I_niz = I[24:]

args, covarian = scipy.optimize.curve_fit(mapping, p_vverh, I_vverh)
args1, covarian1 = scipy.optimize.curve_fit(mapping, p_niz, I_niz)

plt.figure(figsize=[10, 8])
plt.errorbar(P, I, xerr=0, yerr=0, fmt='b.')
plt.errorbar(np.linspace(P[0], P[len(P) - 1]), np.linspace(P[0], P[len(P) - 1]) * args[0] + args[1], xerr=0, yerr=0, fmt='g--')
plt.errorbar(np.linspace(P[0], P[len(P) - 1]), np.linspace(P[0], P[len(P) - 1]) * args1[0] + args1[1], xerr=0, yerr=0, fmt='r--')
plt.errorbar(np.array([(args[1] - args1[1]) / (args1[0] - args[0])]), np.array([(args[1] - args1[1]) / (args1[0] - args[0])]) * args[0] + args[1], xerr=0, yerr=0, fmt='g*')
print("x: ", (args[1] - args1[1]) / (args1[0] - args[0]), "y: ", (args[1] - args1[1]) / (args1[0] - args[0]) * args[0] + args[1])
plt.xlabel("P, кПа")
plt.ylabel("I, pA")
plt.show()
