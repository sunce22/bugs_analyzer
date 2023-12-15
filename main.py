import pandas as pd

# Завантажимо файли
file1 = 'Баги найденые в процесе регреса - Спринт 43.csv'
file2 = 'Баги найденые в процесе регреса - Спринт 44.csv'

# Зчитаємо файли у DataFrame
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Виберемо 1 колонку з кожного файлу та виділимо числа після знаку "-"
df1['Число'] = df1['Линк на задачу'].str.split('-').str[-1].astype(int)
df2['Число'] = df2['Линк на задачу'].str.split('-').str[-1].astype(int)

numbers_df1 = df1['Число'].tolist()
numbers_df2 = df2['Число'].tolist()

# Знайдемо числа, які повторюються в обох списках
common_numbers = list(set(numbers_df1).intersection(numbers_df2))

# Знайдемо числа, які унікальні для кожного списку
unique_numbers_df1 = list(set(numbers_df1) - set(numbers_df2))
unique_numbers_df2 = list(set(numbers_df2) - set(numbers_df1))

# Виведемо результати
print("Кількість повторюваних багів", len(common_numbers))
print("Унікальні для першого списку:", unique_numbers_df1)
print("Унікальні для другого списку:", unique_numbers_df2)
