import math
import numpy as np
from scipy.optimize import minimize, differential_evolution


def f(x):
    return math.sin(x/5) * math.exp(x/10) + 5 * math.exp(-x/2)


x = [(1, 30)]
x0 = np.array([2])

res = minimize(f, x0, method='BFGS')
m1 = f(res.x[0])
print(m1)

x0 = np.array([30])
res = minimize(f, x0, method='BFGS')
m2 = f(res.x[0])
print(m2)

m = str(round(m1, 2)) + " " + str(round(m2, 2))

with open("out1.txt", "w") as out:
    out.write(m)