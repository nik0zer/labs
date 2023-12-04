import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

def mapping(x, a, b):
    return a * x + b

V = list()
I_V = list()


with  open('data_4', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        V.append(list_line[0])
        I_V.append(list_line[1])

V = np.array(V)
I_V = np.array(I_V)
I_V = np.sqrt(I_V)




args, covarian = scipy.optimize.curve_fit(mapping, V, I_V)
a, b = args[0], args[1]

plt.errorbar(np.linspace(0, 3, 1024), np.linspace(0, 3, 1024) * a + b, fmt="g--")
plt.errorbar(V, I_V, fmt="b.")

plt.xlabel("V, В")
plt.ylabel("sqrt(I), sqrt(В)")
print(args, np.sqrt(np.diag(covarian)), -args[1] / args[0])
plt.show()

