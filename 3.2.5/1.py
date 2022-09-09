import matplotlib.pyplot as plt
import numpy as np

R_0_list_u = []
R_0_list_v = []
R_1_list = []

with  open('data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        R_0_list_u.append(list_line[0] / 100.0)
        R_0_list_v.append(list_line[1] / 1575.0)

x = np.array(R_0_list_v)
y = np.array(R_0_list_u)

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

ax.set_ylabel("U/Um")
ax.set_xlabel("V/Vm")
ax.set_title("resonance curve for R = 0 Om")

plt.plot(x, y, 'r')

print(R_0_list_v[23] - R_0_list_v[11])

plt.savefig("1.png")