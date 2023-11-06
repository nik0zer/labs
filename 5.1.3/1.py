import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

V_in = list()
V_ak_net = list()

with  open('data_1', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        V_in.append(list_line[0])
        V_ak_net.append(list_line[1])


plt.figure(figsize=[20, 10])
plt.errorbar(V_in, V_ak_net, xerr=0, yerr=0, fmt='b.')
plt.ylabel("V, анод-катод В")
plt.xlabel("V, катод В")
plt.show()