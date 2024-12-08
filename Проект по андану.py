#Импортируем pandas
import pandas as pd

#Открываем датасет
df = pd.read_csv('E:\Учёба\Анализ данных\Mental health Depression disorder Data')
df.tail()

#Выделяем первую таблицу из всего датасета
normal_table = df.iloc[:6468].copy()
normal_table

df.iloc[6466:6476]
df.iloc[54270:54286]

#Убираем колонку "Индекс" и приводим значения колонок к нужным типаи
normal_df = normal_table.drop(columns=["index"])
normal_df["Schizophrenia (%)"] = normal_df["Schizophrenia (%)"].astype(float)
normal_df["Bipolar disorder (%)"] = normal_df["Bipolar disorder (%)"].astype(float)
normal_df["Eating disorders (%)"] = normal_df["Eating disorders (%)"].astype(float)
normal_df["Year"] = normal_df["Year"].astype(int)
normal_df[normal_df.isnull().any(axis=1)].Entity.unique()
normal_df

#Выводим инфу о датасете для описания
normal_df.info()

#Делаем первую фильтрацию (5 условий)
normal_df.sort_values(['Schizophrenia (%)', 'Bipolar disorder (%)', 'Eating disorders (%)', 'Anxiety disorders (%)', 'Depression (%)'])

#Делаем вторую фильтрацию (3 условия)
res_1 = normal_df.sort_values(['Alcohol use disorders (%)', 'Depression (%)', 'Drug use disorders (%)'])
res_1.head(28)

#Импортируем matplotlib и строим частотные таблицы
import matplotlib.pyplot as plt

# Топ-5 стран с наибольшим ростом уровня шизофрении
schizophrenia_growth = normal_df.groupby('Entity').apply(lambda x: x.loc[x['Year'].idxmax()]['Schizophrenia (%)'] - x.loc[x['Year'].idxmin()]['Schizophrenia (%)'])
top_5_schizophrenia_growth = schizophrenia_growth.sort_values(ascending=False).head(5)
print("Топ-5 стран с наибольшим ростом уровня шизофрении:")
print(top_5_schizophrenia_growth, "\n")

# Топ-5 стран по депрессии
depression_by_country = normal_df.groupby('Entity')['Depression (%)'].mean().sort_values(ascending=False)
print("Топ-5 стран по среднему уровню депрессии:")
print(depression_by_country.head(5), "\n")

# Топ-5 стран по тревожным расстройствам
anxiety_by_country = normal_df.groupby('Entity')['Anxiety disorders (%)'].mean().sort_values(ascending=False)
print("Топ-5 стран по среднему уровню тревожных расстройств:")
print(anxiety_by_country.head(5), "\n")

# Топ-5 стран по употреблению наркотиков
drug_use_by_country = normal_df.groupby('Entity')['Drug use disorders (%)'].mean().sort_values(ascending=False)
print("Топ-5 стран по среднему уровню употребления наркотиков:")
print(drug_use_by_country.head(5), "\n")

