import math
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x/5) * math.exp(x/10) + 5 * math.exp(-x/2)


def make_A(x, n):
    A = np.ones((n,n))
    for i in range(n):
        for j in range(n):
            A[i][j] = x[i] ** j
    return A

def make_b(x, n):
    b = np.ones((n, 1))
    for i in range(n):
        b[i][0] = f(x[i])
    return b

def polynom(w, x, n):
    p = 0
    for i in range(n):
        p += w[i] * (x ** i)
    return p


# x = [1, 15]
# x = [1, 8, 15]
x = [1, 4, 10, 15]

A = make_A(x, len(x))
b = make_b(x, len(x))

W = linalg.solve(A, b)
print(W)

x1 = np.linspace(1, 15, 100)
fx1 = [f(x1[i]) for i in range(len(x1))]
pol = [polynom(W, x1[i], len(x)) for i in range(len(x1))]

plt.plot(x1, fx1)
plt.plot(x1, pol)
plt.show()

m = str(W[0][0]) + " " + str(W[1][0]) + " " + str(W[2][0]) + " " + str(W[3][0])

with open("out2.txt", "w") as out:
    out.write(m)




