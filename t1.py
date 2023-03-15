from main_read_files import read_files

file_values = read_files()

all_data = {}
for file_value in file_values:
    if file_value and file_value[1]:
        all_data[file_value[0]] = float(file_value[1])

min_temp_year = min(all_data, key=all_data.get)

print("Min Temp :", all_data[min_temp_year], "in", min_temp_year)