import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

# def mapping(x, a, b):
#     return a * x + b

V = list()
I_V = list()


with  open('data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        V.append(list_line[0])
        I_V.append(list_line[1] - 0.018)


plt.errorbar(V, I_V, fmt="b.")

plt.xlabel("V, В")
plt.ylabel("I, В")
plt.show()
