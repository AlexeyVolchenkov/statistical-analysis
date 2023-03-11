from read_file import read_file
from count_const import number_of_groups, interval_length
from interval_distribution_series import dicts_of_age, get_keys, getting_the_result_interval, properties
from plotting import plotting_dist

data = []
data_uniq = []
arr_of_dicts = []
keys = []
keysv2 = []
new_arr_of_dicts = []
names_intervals = []

data = read_file(data)

print("Количество элементов: ", len(data))

m = number_of_groups(data)
h = interval_length(data, m)

data = sorted(data)
data_unique = set(data)

dicts_of_age(data, data_unique, arr_of_dicts)

print("Количество человек, каждого возраста: ", arr_of_dicts)

get_keys(arr_of_dicts, keys)

getting_the_result_interval(data, keys, arr_of_dicts, new_arr_of_dicts, h, names_intervals)

print("Количество человек попадающие в выбранные интервалы: ", new_arr_of_dicts)

properties(min(data), m, h, keys[-1][0], new_arr_of_dicts, names_intervals, new_arr_of_dicts)

for i in keys:
    keysv2.append(i[0])

plotting_dist(arr_of_dicts, keysv2)

plotting_dist(new_arr_of_dicts, names_intervals)
