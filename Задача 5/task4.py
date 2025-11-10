import numpy as np
from scipy.stats import hypergeom
import pandas as pd
import matplotlib.pyplot as plt

[N, M, n] = 50, 20, 12

X = np.arange(0, n + 1)
geom_dist = hypergeom(M=N, n=M, N=n)
probabilities = geom_dist.pmf(X)

df = pd.DataFrame(data=probabilities.reshape(1, -1),
                 columns = X,
                 index=['p'])
df

print(f'Мат. ожидание = {geom_dist.mean():.4f}')
print(f'Дисперсия = {geom_dist.var():.4f}')
print(f'Среднее квадратическое отклонение = {geom_dist.std():.4f}')

max_prob = probabilities.max()
mode_index = np.argmax(probabilities)
mode = X[mode_index]
print(f'Мода = {mode}')

plt.figure(figsize=(4,2))

plt.plot(X, probabilities, '-ro', ms=8, label = 'hypergeom pmf')
plt.show();
