import numpy as np
from scipy.stats import geom
import pandas as pd
import matplotlib.pyplot as plt

p = 0.06

K = np.arange(1, 14)
geom_dist = geom(p)
probabilities = geom_dist.pmf(K)

df = pd.DataFrame(data=probabilities.reshape(1, -1),
                 columns = X,
                 index=['p'])
df

print(f'Мат. ожидание = {geom_dist.mean():.4f}')
print(f'Дисперсия = {geom_dist.var():.4f}')
print(f'Среднее квадратическое отклонение = {geom_dist.std():.4f}')

max_prob = probabilities.max()
mode_index = np.argmax(probabilities)
mode = K[mode_index]
print(f'Мода = {mode}')

plt.figure(figsize=(4,2))

plt.plot(K, probabilities, 'mo', ms=8, label='geom pmf')
plt.vlines(K, 0, probabilities, colors='m', lw=2, alpha=0.5)

plt.legend(loc='best', frameon=False)
plt.show();
