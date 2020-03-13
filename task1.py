import re
import numpy as np
from scipy.spatial import distance

lst = []
with open("sentences.txt") as sentences:
    for data in sentences:
        data = re.split('[^a-z]', data.lower())
        lst.append([d for d in data if d])


words = {}
d = 0
for i in lst:
    for j in i:
        if j not in words.values():
            words[d] = j
            d += 1

matrix = np.zeros((len(lst), d))
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        for k in range(len(lst[i])):
            if words[j] == lst[i][k]:
                matrix[i][j] += 1

print(matrix)

dist = []
i = matrix[0]
for j in range(1, len(matrix)):
    dist.append(distance.cosine(i, matrix[j]))
print(dist)

s1 = min(dist)
s2 = max(dist)
print(len(dist))
for i in range(len(dist)):
    if dist[i] == s1:
        m1 = i + 1
    if dist[i] < s2 and dist[i] != s1:
        s2 = dist[i]
        m2 = i + 1

m = str(m1) + " " + str(m2)

with open("out.txt", "w") as out:
    out.write(m)




