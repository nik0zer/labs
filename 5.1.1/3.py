import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

def mapping(x, a, b):
    return a * x + b

W = list()
V = list()


with  open('data3', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        W.append(2* np.pi *3 * 10 ** 8 / (list_line[0] * 10 ** -10))
        V.append(list_line[1])

W = np.array(W)
V = np.array(V)




args, covarian = scipy.optimize.curve_fit(mapping, W, V)
a, b = args[0], args[1]

plt.errorbar(np.linspace(min(W), max(W), 1024), np.linspace(min(W), max(W), 1024) * a + b, fmt="g--")
plt.errorbar(W, V, fmt="b.")

plt.xlabel("W, Гц")
plt.ylabel("V, В")
print(args, np.sqrt(np.diag(covarian)))
plt.show()

