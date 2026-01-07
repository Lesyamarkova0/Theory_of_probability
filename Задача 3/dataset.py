import numpy as np
import pandas as pd

data = pd.read_csv("data_set.csv")

data

print('Размерность данных', data.shape)

data.head()

print("\nСтолбцы:", data.columns.tolist())

data.info()

# Пропущенные значения 
print('\nПропущенные значения:')
missing_data = data.isnull().sum()
missing_percent = (missing_data / len(data)) * 100
missing_df = pd.DataFrame({'Количество пропусков': missing_data,
             'Процент пропусков': missing_percent.round(2)})
print(missing_df)

print('\nДоля студентов с высокой оценкой по посещению платных занятий:')

pivot = pd.pivot_table(
    data.assign(high_grade = data['G3'] >= 15),
    values = 'high_grade',
    index = ['paid'],
    columns = ['sex'],
    aggfunc = 'mean',
    fill_value = 0
)

print(pivot.round(4))

P_high_grade = (data['G3'] >= 15).mean()
print(f'\nP(G3 >= 15) = {P_high_grade:.4f}')

P_paid = (data['paid'] == 'yes').mean()
print(f'\nP(paid = yes) = {P_paid:.4f}')

P_internet = (data['internet'] == 'yes').mean()
print(f'\nP(internet = yes) = {P_internet:.4f}')

data['high_grade'] = (data['G3'] >= 15)

P_high_paid = ((data['high_grade'] == True) & (data['paid'] == 'yes')).mean()
P_paid = (data['paid'] == 'yes').mean()
P = P_high_paid / P_paid
print(f'\nP(high_grade | paid), рассчитанная вручную: {P:.4f}')

paid_yes = data[data['paid'] == 'yes']
P_filtered = paid_yes['high_grade'].mean()
print(f'\nP(high_grade | paid), рассчитанная через фильтр: {P_filtered:.4f}')

P_high_famsup = ((data['high_grade'] == True) & (data['famsup'] == 'yes')).mean()
P_famsup = (data['famsup'] == 'yes').mean()
P = P_high_famsup / P_famsup
print(f'\nP(high_grade | famsup), рассчитанная вручную: {P:.4f}')

famsup_yes = data[data['famsup'] == 'yes']
P_filtered = famsup_yes['high_grade'].mean()
print(f'\nP(high_grade | famsup), рассчитанная через фильтер: {P_filtered:.4f}')

P_urban_internet = ((data['address'] == 'U') & (data['internet'] == 'yes')).mean()
P_internet = (data['internet'] == 'yes').mean()
P = P_urban_internet / P_internet
print(f'\nP(address | internet), рассчитанная вручную: {P:.4f}')

internet_yes = data[data['internet'] == 'yes']
P_filtered = (internet_yes['address'] == 'U').mean()
print(f'\nP(address | internet), рассчитанная через фильтер: {P_filtered:.4f}')
