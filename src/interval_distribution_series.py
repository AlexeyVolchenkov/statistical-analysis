def dicts_of_age(data, data_unique, arr_of_dicts):
    for i in data_unique:
        arr_of_dicts.append({i: data.count(i)})


def get_keys(arr_of_dicts, keys):
    for i in arr_of_dicts:
        keys.append(list(i.keys()))


def getting_the_result_interval(data, keys, arr_of_dicts, new_arr_of_dicts, h):
    total = 0
    j = 0
    number_first = number = data[0]
    for i in keys:
        total += arr_of_dicts[j][i[0]]

        if arr_of_dicts[-1] == arr_of_dicts[j]:
            new_arr_of_dicts.append({str(number) + ' - ' + str(keys[-1][0]): total})
            total = 0
        j += 1
        if j % h == 0 and j != 0:
            new_arr_of_dicts.append({str(number_first + j - h) + ' - ' + str(number_first + j): total})
            number = number_first + j
            total = 0
