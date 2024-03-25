import csv
data = [
    ["Иван", "Иванов", 30],
    ["Мария", "Петрова", 25],
    ["Алексей", "Сидоров", 35]
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Имя", "Фамилия", "Возраст"])
    writer.writerows(data)

def read_csv_file(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'Имя: {row[0]}, Фамилия: {row[1]}, Возраст: {row[2]}')

read_csv_file('data.csv')
