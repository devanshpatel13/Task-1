result = []
new_array = []
last_array = 0
array = [1, 7, 11, 18, 29, 47,76, 0, 8, -1, 0, 1, 1, 2, 3, 5, 8, 13, -10, 4, 10]
a_length = len(array)
for idx, value in enumerate(array):
    if idx+2 >= a_length:
        break
    if array[idx]+array[idx+1] == array[idx+2]:
        new_array.append(array[idx])
    else:
        if new_array:
            new_array.append(array[idx])
            new_array.append(array[idx+1])
            result.append(new_array)
        new_array = []
print(result)