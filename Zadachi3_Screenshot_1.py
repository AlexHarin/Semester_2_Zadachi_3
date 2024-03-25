file_name = "ехample.txt"
with open(file_name, "w") as file:
    file.write("Привет, это содержимое файла 'ехample'.\n")
    file.write("Это вторая строка текста.\n")
    file.write("И еще одна строка для примера.\n")
def print_file_content(file_name):
    with open(file_name, "r") as file:
        for line in file:
            print(line, end="")
print_file_content("ехample.txt")
