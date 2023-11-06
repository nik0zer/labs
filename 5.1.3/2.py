import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

V_in = list()
V_ak_net = list()

with  open('data_2', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        V_in.append(list_line[0])
        V_ak_net.append(list_line[1])


V_in = np.array(V_in)
V_ak_net = np.array(V_ak_net)

plt.figure(figsize=[8, 4])
plt.errorbar(V_in , -np.log(V_ak_net / 165.7), xerr=0, yerr=0, fmt='b.')
plt.ylabel("Вероятность рассеяния")
plt.xlabel("V, катод В")
plt.show()