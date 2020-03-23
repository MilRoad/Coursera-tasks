import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize, differential_evolution


def f(x):
    return math.sin(x/5) * math.exp(x/10) + 5 * math.exp(-x/2)

def h(x):
    return int(f(x))

# график h(x)
# x1 = np.linspace(1, 30, 100)
# fx1 = [h(x1[i]) for i in range(len(x1))]
#
# plt.plot(x1, fx1)
# plt.show()


x0 = np.array([30])
res = minimize(h, x0, method='BFGS')
m1 = h(res.x[0])

x = [(1, 30)]
res = differential_evolution(f, x)
m2 = h(res.x[0])

m = str(round(m1, 2)) + " " + str(round(m2, 2))

with open("out3.txt", "w") as out:
    out.write(m)