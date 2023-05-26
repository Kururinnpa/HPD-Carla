import matplotlib.pyplot as plt
import numpy as np

filename = '3-3-3'
file = open('./'+filename+'.txt', 'r')

plt.xlim(-300, 10300)
plt.ylim(-1, 11)
plt.xticks(np.linspace(0, 10000, 11))
plt.yticks(np.linspace(0, 10, 6))
n = 0
s = []
frames = 0
while n < 11500:
    line = file.readline()
    if n >= 1500:
        a = float(line.split()[0])
        s.append(a)
        frames += a
    n += 1
plt.plot(np.linspace(0, 10000, 10000), s)
plt.title("three servers three cars-3")
plt.savefig(filename)
plt.show()
print(frames / 10000)
file.close()