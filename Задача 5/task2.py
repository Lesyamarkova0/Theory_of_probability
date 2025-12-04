import numpy as np
from scipy.stats import poisson
import pandas as pd
import matplotlib.pyplot as plt

lmb = 3

X = np.arange(0, 10)

poisson_dist = poisson(lmb)
probabilities = poisson_dist.pmf(X)

df = pd.DataFrame(data=probabilities.reshape(1, -1), columns = X, index=['p'])
df

print(f'Мат. ожидание = {poisson_dist.mean():.4f}')
print(f'Дисперсия = {poisson_dist.var():.4f}')
print(f'Среднее квадратическое отклонение = {poisson_dist.std():.4f}')

max_prob = probabilities.max()
mode = [int(x) for x in X if round(probabilities[x], 6)==round(max_prob, 6)]
print(f'Мода = {mode}')

plt.figure(figsize=(8,3))
plt.plot(X, probabilities, 'o-', color='red',  linewidth=2, markersize=6)
plt.title(f'Распределение Пуассона')
plt.xlabel('Число заказов за 10 минут, m')
plt.ylabel('Вероятность, P(X=m)')
plt.xticks(X)
plt.grid(axis='y', alpha=0.75)
plt.show()
