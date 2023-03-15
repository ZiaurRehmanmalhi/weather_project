from main_read_files import read_files
file_values = read_files()

# for file_value in file_values:
#     print(file_value)

all_data = {}
for file_value in file_values:
    if file_value and file_value[1]:
        all_data[file_value[0]] = float(file_value[1])

max_temp_year = max(all_data, key=all_data.get)

print("Max Temp :", all_data[max_temp_year], "in", max_temp_year)
