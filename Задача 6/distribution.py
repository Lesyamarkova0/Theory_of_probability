import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_continuous
from scipy import integrate

class CustomDistribution(rv_continuous):
    def __init__(self, a, b):
        super().__init__(a = a, b = b, name = 'custom_dist')
    
    def _pdf(self, x):
        "Плотность распределения"
        result = np.zeros_like(x)
        result[(x >= self.a) & (x <= self.b)] = 6 * x - 6 * x ** 2
        return result
    
    def _cdf(self, x):
        "Функция распределения"
        result = np.zeros_like(x)
        result[x < self.a] = 0
        result[(x >= self.a) & (x <= self.b)] = 3 * x ** 2 - 2 * x ** 3
        result[x > self.b] = 1
        return result
    
a, b = 0.0, 1.0
custom_dist = CustomDistribution(a, b) #создаем экземпляр распределния

sample = custom_dist.rvs(size = 10000)

print(f'Размер выборки: {len(sample)}')
print(f'Первые 10 значений: {sample[:10]}')

x_test = np.linspace(a - 0.5, b + 0.5, 100)
pdf_values = custom_dist.pdf(x_test)
cdf_values = custom_dist.cdf(x_test)

# проверка условия нормировки плотности
print('\nПроверка нормировки плотности:')
integral, error = integrate.quad(custom_dist.pdf, a, b)
print(f'∫f(x)dx на [{a, b}] = {integral:.6f} (ошибка: {error:.2e})')

print('\nПроверка в граничных точках:')
print(f'F({a}) = {custom_dist.cdf(a):.6f}')
print(f'F({b}) = {custom_dist.cdf(b):.6f}')

# вероятность попадания случайной величины в некоторый интервал [0.2, 0.7]
print(f'\nВероятность попадания СВ Х в интервал [0.2, 0.7]: P(0.2 <= X <= 0.7) = {custom_dist.cdf(0.7) - custom_dist.cdf(0.2)}')

print()

# вычисление числовых характеристик
print('ЧИСЛОВЫЕ ХАРАКТЕРИСТИКИ'.center(50, '*'))
print(f'\nМатематическое ожидание: {custom_dist.mean():.4f}')
print(f'\nДисперсия: {custom_dist.var():.4f}')
print(f'\nСреднее квадратическое отклонение: {custom_dist.std():.4f}')

# вычисление квантиля уровня 40% и 80%-ую точку св
print(f'\n40%-квантиль: {custom_dist.ppf(0.4):.4f}')
print(f'80%-ая точка: {custom_dist.ppf(0.8):.4f}')

skew, kurt = custom_dist.stats(moments = 'sk')
print(f'\nАсимметрия: {skew:.4f}')
print(f'Эксцесс: {kurt:.4f}')

# построение графиков
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5))
x_plot = np.linspace(a - 0.2, b + 0.2, 1000)

# 1. функция распределния
ax1.hist(sample, bins = 50, density = True, cumulative = True,
        alpha = 0.7, label = 'Эмпирическая CDF')
ax1.plot(x_plot, custom_dist.cdf(x_plot), 'r-', linewidth = 2, 
        label = 'Теоретическая CDF')
ax1.set_xlabel('x')
ax1.set_ylabel('F(x)')
ax1.set_title('Функция распределения')
ax1.legend()
ax1.grid(True, alpha = 0.3)

# 2. Гистограмма и теоретическая плотность
ax2.hist(sample, bins = 50, density = True, alpha = 0.7, 
         label = 'Выборка')
ax2.plot(x_plot, custom_dist.pdf(x_plot), 'r-', linewidth = 2, 
        label = 'Теоретическая PDF')
ax2.set_xlabel('x')
ax2.set_ylabel('Плотность вероятности')
ax2.set_title('Гистограмма и теоретическая плотность')
ax2.legend()
ax2.grid(True, alpha = 0.3)

plt.show()
