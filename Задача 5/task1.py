import numpy as np
from scipy.stats import binom
import pandas as pd
import matplotlib.pyplot as plt

n, p = 7, 0.4
X = np.arange(0, n + 1)

binomial_dist = binom(n, p)
probabilities = binomial_dist.pmf(X)

df = pd.DataFrame(data=probabilities.reshape(1, -1),
                 columns = X,
                 index=['p'])
df

print(f'Мат. ожидание = {binomial_dist.mean():.4f}')
print(f'Дисперсия = {binomial_dist.var():.4f}')
print(f'Среднее квадратическое отклонение = {binomial_dist.std():.4f}')

max_prob = probabilities.max()
mode = [int(x) for x in X if round(probabilities[x], 6)==round(max_prob, 6)]
print(f'Мода = {mode}')

plt.figure(figsize=(8,3))
plt.bar(X, probabilities, color='coral', edgecolor='black', alpha = 0.7)
plt.title(f'Биномиальное распределение (n={n}, p={p})')
plt.xlabel('Число падений программы, m')
plt.ylabel('Вероятность, P(X=m)')
plt.xticks(X)
plt.grid(axis='y', alpha=0.75)
plt.show()
