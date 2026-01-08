### Применение условных вероятностей в анализе данных

## О датасете

Датасет Student Performance Dataset содержит информацию об успеваемости учащихся.

Всего 33 признака.

Целевая переменная: G3 - итоговая оценка по предмету в конце семестра. Это числовая переменная.
Дополнительные целевые переменные: G1 и G2 - оценки за первый и второй семестры соответственно.

Источник датасета: 
[Student Performance Dataset](https://www.kaggle.com/datasets/devansodariya/student-performance-data?resource=download)

---

## Описание признаков
- 

---

## Вычисление простых вероятностей

Вычислим некоторые априорные вероятности по формуле:

$$
P(A) = \frac{\text{Число случаев A}}{\text{Обшее число}}
$$

1. Вероятность получить высокую оценку.

``` python
P_high_grade = (data['G3'] >= 15).mean()
print(f'P(G3 >= 15) = {P_high_grade:.4f}')
```

$$
P(G3 >= 15) = 0.1848
$$

2. Вероятность посещать платные занятия.

```python
P_paid = (data['paid'] == 'yes').mean()
print(f'P(paid = yes) = {P_paid:.4f}')
```

$$
P(paid = yes) = 0.4582
$$

3. Вероятность иметь домашний интернет.

```python
P_internet = (data['internet'] == 'yes').mean()
print(f'P(internet = yes) = {P_internet:.4f}')
```

$$
P(internet = yes) = 0.8329
$$

---

## Вычисление условных вероятностей

Условную вероятность можно вычислить по следующей формуле:

$$

$$

1. Какова вероятность улучшить итоговую оценку, если студент посещает дополнительные платные занятия?

```python
# Способ 1: Вручную по формуле
data['high_grade'] = (data['G3'] >= 15)

P_high_paid = ((data['high_grade'] == True) & (data['paid'] == 'yes')).mean()
P_paid = (data['paid'] == 'yes').mean()
P = P_high_paid / P_paid

print(f'P(high_grade | paid = yes), рассчитанная вручную: {P:.4f}')
```

$$
\text{P(high grade | paid = yes), рассчитанная вручную: } 0.1768
$$

```python
# Способ 2: Просто отфильтровав датафрейм и посчитав среднее 
paid_yes = data[data['paid'] == 'yes']
P_filtered = paid_yes['high_grade'].mean()

print(f'P(high_grade | paid = yes), рассчитанная через фильтр: {P_filtered:.4f}')
```

$$
\text{P(high grade | paid = yes), рассчитанная через фильтр: } 0.1768
$$

2. Какова вероятность получить итоговую высокую оценку, если студент имеет семейную поддержку?

```python
# Способ 1: Вручную по формуле
P_high_famsup = ((data['high_grade'] == True) & (data['famsup'] == 'yes')).mean()
P_famsup = (data['famsup'] == 'yes').mean()
P = P_high_famsup / P_famsup

print(f'P(high_grade | famsup = yes), рассчитанная вручную: {P:.4f}')
```

$$
\text{P(high_grade | famsup = yes), рассчитанная вручную: } 0.1736
$$

```python
# Способ 2: Просто отфильтровав датафрейм и посчитав среднее 
famsup_yes = data[data['famsup'] == 'yes']
P_filtered = famsup_yes['high_grade'].mean()

print(f'P(high_grade | famsup = yes), рассчитанная через фильтер: {P_filtered:.4f}')
```

$$
\text{P(high_grade | famsup = yes), рассчитанная через фильтер: } 0.1736
$$

3. Какова вероятность, что студент живет в городе, если у него есть домашний интернет?

```python
# Способ 1: Вручную по формуле
P_urban_internet = ((data['address'] == 'U') & (data['internet'] == 'yes')).mean()
P_internet = (data['internet'] == 'yes').mean()
P = P_urban_internet / P_internet

print(f'P(address | internet = yes), рассчитанная вручную: {P:.4f}')
```

$$
\text{P(address | internet = yes), рассчитанная вручную: } 0.8176
$$

```python
# Способ 2: Просто отфильтровав датафрейм и посчитав среднее 
internet_yes = data[data['internet'] == 'yes']
P_filtered = (internet_yes['address'] == 'U').mean()

print(f'P(address | internet = yes), рассчитанная через фильтер: {P_filtered:.4f}')
```

$$
\text{P(address | internet = yes), рассчитанная через фильтер: } 0.8176
$$
