import matplotlib.pyplot as plt
import numpy as np

R_0_list_u = []
R_0_list_v = []

R_0_list_u_1 = []
R_0_list_v_1 = []


with  open('data', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        R_0_list_u.append(list_line[0] / 100.0)
        R_0_list_v.append(list_line[1] / 1575.0)

with  open('data1', 'r')  as  data:
    for line in data:
        list_line = list((map(float, line.split())))
        R_0_list_u_1.append(list_line[0] / 100.0)
        R_0_list_v_1.append(list_line[1] / 1575.0)

x = np.array(R_0_list_v)
y = np.array(R_0_list_u)

x1 = np.array(R_0_list_v_1)
y1 = np.array(R_0_list_u_1)

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

ax.set_ylabel("U/Um")
ax.set_xlabel("V/Vm")
ax.set_title("resonance curves for R = 0 Om and R = 100 Om")

plt.plot(x, y, 'r', x1, y1, 'g')

print(R_0_list_v[23] - R_0_list_v[11])

plt.savefig("3.png")