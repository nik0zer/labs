import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

def mapping(x, a, b):
    return a * x + b

S = 0.36

T = list()
e = list()
I = list()
V = list()

with  open('data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        I.append(list_line[0])
        V.append(list_line[1])
        T.append(list_line[2])
        e.append(list_line[3])

plt.figure(figsize=[8, 8])

I = np.array(I)
T = np.array(T)
e = np.array(e)
V = np.array(V)

x = np.log(np.array(T))
y = np.log(np.array(I * V / 1000))

args, covarian = scipy.optimize.curve_fit(mapping, x, y)
a, b = args[0], args[1]

teor_x = np.linspace(min(x), max(x), 1024)
teor_y = a * teor_x + b

plt.plot(x, y, 'b.')
plt.plot(teor_x, teor_y, 'g--')

plt.xlabel("ln(T)")
plt.ylabel("ln(W)")

perr = np.sqrt(np.diag(covarian))
print("a:", a, "error_rate a:", perr[0], "b:", b, "error_rate b:", perr[1])


sigma = (I * V) / (e * S * T ** 4)
h = np.power(np.divide((2 * np.pi ** 5 / (1.38 ** 23)), (15 * (3 * 10 ** 8) ** 2 * sigma)), 1 / 3)
print(sigma)
print(sum(sigma) / len(sigma))
print(h)
print(sum(h) / len(h))

plt.show()