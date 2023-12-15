import pandas as pd
import re
def remove_spaces_and_quotes(input_file, output_file):
    # Зчитування даних з CSV-файлу
    df = pd.read_csv(input_file)

    # Обробка даних: видалення пробілів і знаків " з усіх значень
    df = df.apply(lambda x: re.sub(r'\s+|"', '', str(x)))

    # Запис даних у новий CSV-файл
    df.to_csv(output_file, index=False)

# Приклад використання:
input_file = 'Електронна таблиця без назви - Аркуш1.csv'
output_file = 'output.csv'
remove_spaces_and_quotes(input_file, output_file)
