import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = []

# технический факультет 
men_technical_faculty = 800
men_technical_accepted = int(men_technical_faculty * 0.60)
women_technical_faculty = 200
women_technical_accepted = int(women_technical_faculty * 0.65)

# гуманитарный факультет
men_humanities_faculty = 200
men_humanities_accepted = int(men_humanities_faculty * 0.20)
women_humanities_faculty = 800
women_humanities_accepted = int(women_humanities_faculty * 0.25)

data.extend([
    {'Пол' : 'Мужчина', 'Факультет' : 'Технический', 'Принят' : True, 
     'Количество' : men_technical_accepted},
    {'Пол' : 'Мужчина', 'Факультет' : 'Технический', 'Принят' : False,
     'Количество' : men_technical_faculty - men_technical_accepted},
    {'Пол' : 'Женщина', 'Факультет' : 'Технический', 'Принят' : True, 
     'Количество' : women_technical_accepted},
    {'Пол' : 'Женщина', 'Факультет' : 'Технический', 'Принят' : False,
     'Количество' : women_technical_faculty - women_technical_accepted},
    
    {'Пол' : 'Мужчина', 'Факультет' : 'Гуманитарный', 'Принят' : True, 
     'Количество' : men_humanities_accepted},
    {'Пол' : 'Мужчина', 'Факультет' : 'Гуманитарный', 'Принят' : False, 
     'Количество' : men_humanities_faculty - men_humanities_accepted},
    {'Пол' : 'Женщина', 'Факультет' : 'Гуманитарный', 'Принят' : True, 
     'Количество' : women_humanities_accepted},
    {'Пол' : 'Женщина', 'Факультет' : 'Гуманитарный', 'Принят' : False, 
     'Количество' : women_humanities_faculty - women_humanities_accepted},
])

df = pd.DataFrame(data)
df = df.loc[df.index.repeat(df['Количество'])].reset_index(drop = True)
df = df.drop(columns = ['Количество'])

all = df.groupby('Пол')['Принят'].agg(['sum', 'size']).reset_index()
all['Процент принятых'] = all['sum'] / all['size']

by_faculty = df.groupby(['Факультет', 'Пол'])['Принят'].agg(['sum', 'size']).reset_index()
by_faculty['Процент принятых'] = by_faculty['sum'] / by_faculty['size']

print('Агрегированные данные (все абитуриенты вместе):')
for _, row in all.iterrows():
    print(f"{row['Пол']}: {row['Процент принятых']:.1%}")
    
print('\nПо факультетам:')
for _, row in by_faculty.iterrows():
    print(f"{row['Факультет']} - {row['Пол']} : {row['Процент принятых']:.1%}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (14, 6))

genders = all['Пол'].tolist()
rates1 = [r * 100 for r in all['Процент принятых']]
bars1 = ax1.bar(genders, rates1, color = ['lightcoral', 'lightblue'], 
                edgecolor = 'black')
ax1.set_title('Все абитуриенты вместе:', fontsize = 14, weight = 'bold')
ax1.set_ylabel('Процент принятых (%)')
ax1.set_ylim(0, 50)

faculties = by_faculty['Факультет'].unique()
x = np.arange(len(faculties))
width = 0.35

men_dict = dict(zip(by_faculty[by_faculty['Пол'] == 'Мужчина']['Факультет'],
                   by_faculty[by_faculty['Пол'] == 'Мужчина']['Процент принятых']))
women_dict = dict(zip(by_faculty[by_faculty['Пол'] == 'Женщина']['Факультет'],
                   by_faculty[by_faculty['Пол'] == 'Женщина']['Процент принятых']))

men_rates = [men_dict.get(fac, 0) * 100 for fac in faculties]
women_rates = [women_dict.get(fac, 0) * 100 for fac in faculties]

bars2_men = ax2.bar(x - width/2, men_rates, width, label = 'Мужчина',
                   color = 'lightblue', edgecolor = 'black')
bars2_women = ax2.bar(x + width/2, women_rates, width, label = 'Женщина',
                   color = 'lightcoral', edgecolor = 'black')

ax2.set_title('По факультетам:', fontsize = 14, weight = 'bold')
ax2.set_ylabel('Процент принятых (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(faculties)
ax2.set_ylim(0, 70)
ax2.legend()

for bar, rate in zip(bars2_men, men_rates):
    if rate > 0:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{rate:.1f}%', ha = 'center', fontweight = 'bold')
        
for bar, rate in zip(bars2_women, women_rates):
    if rate > 0:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{rate:.1f}%', ha = 'center', fontweight = 'bold')   
        
plt.tight_layout()
plt.show()
