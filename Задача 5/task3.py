import numpy as np
from scipy.stats import geom
import pandas as pd
import matplotlib.pyplot as plt

p = 0.06

X = np.arange(1, 11)
geom_dist = geom(p)
probabilities = geom_dist.pmf(X)

df = pd.DataFrame(data=probabilities.reshape(1, -1), columns = X, index=['p'])
df

print(f'Мат. ожидание = {geom_dist.mean():.4f}')
print(f'Дисперсия = {geom_dist.var():.4f}')
print(f'Среднее квадратическое отклонение = {geom_dist.std():.4f}')

max_prob = probabilities.max()
mode = [int(x) for x in X if round(probabilities[x - 1], 6) == round(max_prob, 6)]
print(f'Мода = {mode}')

plt.figure(figsize=(8,3))
plt.plot(X, probabilities, 'o-', color='m',  linewidth=2, markersize=6)
plt.title(f'Геометрическое распределение (p = {p})')
plt.xlabel('Количество бросков до первого попадания, m')
plt.ylabel('Вероятность, P(X=m)')
plt.xticks(X)
plt.grid(axis='y', alpha=0.75)
plt.show()
