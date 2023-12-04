import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

def mapping(x, a, b):
    return a * x + b

P = list()
N = list()


with  open('data_2', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        P.append(100 - list_line[0] * 133 / 1000 - 2)
        N.append(list_line[1])


args, covarian = scipy.optimize.curve_fit(mapping, P, N)


plt.figure(figsize=[10, 8])
plt.errorbar(P, N, xerr=0, yerr=0, fmt='b.')
N_new = list()
for i in range(1, len(N) - 1):
    N_new.append(-10 * (N[i + 1] - N[i - 1]) / (P[i + 1] - P[i - 1]))
plt.errorbar(P[1: len(P) - 1], N_new, xerr=0, yerr=0, fmt='r.')

max = 0
max_n = 0
for i in range(len(N_new)):
    if max < N_new[i]:
        max = N_new[i]
        max_n = i

print(P[max_n])

args, covarian = scipy.optimize.curve_fit(mapping, P[2:13], N[2:13])
plt.errorbar(np.linspace(P[2], P[14]), np.linspace(P[2], P[14]) * args[0] + args[1], xerr=0, yerr=0, fmt='g--')
print(-args[1] / args[0])

plt.xlabel("P, кПа")
plt.ylabel("N, частиц")

plt.show()
