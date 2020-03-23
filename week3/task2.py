import math
from scipy.optimize import differential_evolution


def f(x):
    return math.sin(x/5) * math.exp(x/10) + 5 * math.exp(-x/2)


x = [(1, 30)]
res = differential_evolution(f, x)
print(res)
m1 = f(res.x[0])

m = str(round(m1, 2))

with open("out2.txt", "w") as out:
    out.write(m)