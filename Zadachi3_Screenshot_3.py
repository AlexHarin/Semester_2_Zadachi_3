import csv

def process_weather_data(file_name):
    total_temperature = 0
    min_temperature = float('inf')
    max_temperature = float('-inf')
    row_count = 0

    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            temperature = float(row['Temperature'])
            total_temperature += temperature
            min_temperature = min(min_temperature, temperature)
            max_temperature = max(max_temperature, temperature)
            row_count += 1

    average_temperature = total_temperature / row_count

    print("Total number of rows processed:", row_count)
    print("Average temperature:", average_temperature)
    print("Minimum temperature:", min_temperature)
    print("Maximum temperature:", max_temperature)

process_weather_data("weather_data.csv")
