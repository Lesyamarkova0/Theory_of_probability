### Исследование зависимости плотности от параметров НСВ в Python

## Теория по χ<sup>2</sup>-распределению

Область определения: x ∈ [0, +∞)

#### Определение
Распределением χ<sup>2</sup> (хи-квадрат) с k степенями свободы называется распределение суммы квадратов k независимых случайных величин, распределенных по стандартному нормальному закону, то есть: 

$$
\chi^2 = \sum_{i=1}^{k} Z_i^2,
$$

где $Z_i \sim \mathcal{N}(0, 1)$ имеет нормальное распределение N(0; 1).

---

## Плотность вероятности χ<sup>2</sup>-распределения имеет вид:

$$
φ(x) = 
\begin{cases}
\displaystyle \frac{1}{2^{k/2} \cdot Г\left(\frac{k}{2}\right)} \cdot x^{(k/2) - 1} \cdot e^{-(x/2)}, & \text{при } x \geq 0, \\
0, & \text{при } x < 0,
\end{cases}
$$

где $Г(y) = \int_0^{+\infty} e^{-t} t^{y-1} \ dt$ - гамма-функция Эйлера (для целых положительных значений $Г(y) = (y - 1)!$). 

---

При k > 30 распределение случайной величины Z = √2χ<sup>2</sup> - √2k-1 близко к стандартному нормальному закону, т.е. N(0; 1).

χ<sup>2</sup>-распределение асимметрично, обладает положительной (правосторонней) асимметрией.

Распределение хи-квадрат является частным случаем гамма-распределениея с гамма-параметрами a = df/2, loc = 0 и scale = 2.

---

## Функция распределения
Для χ<sup>2</sup>-распределения с k-степенями свободы функция распределения имеет вид:

$$
F(X) = \frac{γ\left( \frac{k}{2}, \frac{x}{2} \right)}{Г\left(\frac{k}{2} \right)},
$$

где $γ(a, x) = \int_0^x t^{a-1} e^{-t} \, dt$ - неполная гамма-функция (одна из специальных функций, т.е. не входящих в число элементарных).

А $Г(y) = \int_0^{+\infty} t^{y-1} e^{-t} \, dt$- обозначает полную гамму-функцию.

---

## Числовые характеристики:
- Математическое ожидание: $M(X) = k$
- Диспресия: $D(X) = 2*k$
- Мода: $Mo(X) = 0 для k < 2, Mo(X) = k - 2, если X >= 2$
- Коэффициент асимметрии: $\sqrt{\frac{8}{k}}$
- Коэффициент эксцесса: $12/k$
- Медиана: примерно $k - 2/3$

---

## Поведение графика плотности для χ<sup>2</sup>-распределения

![](https://github.com/Lesyamarkova0/Theory_of_probability/blob/main/Задача%207/chi2-distribution.png)
![](https://github.com/Lesyamarkova0/Theory_of_probability/blob/main/Задача%207/chi2-distribution2.png)

---

## Поведение графика плотности для равномерного распределения
![](https://github.com/Lesyamarkova0/Theory_of_probability/blob/main/Задача%207/uniform_distribution.png)
![](https://github.com/Lesyamarkova0/Theory_of_probability/blob/main/Задача%207/uniform_distribution2.png)

---

## Поведение графика плотности для экспоненциального распределения
![](https://github.com/Lesyamarkova0/Theory_of_probability/blob/main/Задача%207/exp_distribution.png)
![](https://github.com/Lesyamarkova0/Theory_of_probability/blob/main/Задача%207/exp2.png)

---

## Поведение графика плотности для нормального распределения
![](https://github.com/Lesyamarkova0/Theory_of_probability/blob/main/Задача%207/norm_distribution.png)
![](https://github.com/Lesyamarkova0/Theory_of_probability/blob/main/Задача%207/norm2.png)
