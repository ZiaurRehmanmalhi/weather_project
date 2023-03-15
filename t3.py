from main_read_files import read_files

file_values = read_files()
dates_with_difference_of_7 = []

for row in file_values:
    max_temp = int(row[1])
    min_temp = 0
    if row[2]:
        min_temp = int(row[2])
    date = row[0]

    if max_temp - min_temp == 7:
        dates_with_difference_of_7.append(date)
        print(date)
