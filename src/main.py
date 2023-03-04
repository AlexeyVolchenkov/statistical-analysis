from read_file import read_file
from count_const import number_of_groups, interval_length
from interval_distribution_series import dicts_of_age, get_keys, getting_the_result_interval

data = []
data_uniq = []
arr_of_dicts = []
keys = []
new_arr_of_dicts = []

data = read_file(data)

m = number_of_groups(data)
h = interval_length(data, m)

data = sorted(data)
data_unique = set(data)

dicts_of_age(data, data_unique, arr_of_dicts)

get_keys(arr_of_dicts, keys)

getting_the_result_interval(data, keys, arr_of_dicts, new_arr_of_dicts, h)

print(new_arr_of_dicts)
