

def closest_number(arr):
    arr.sort()
    new_array = []  # append closest numbers to new array
    arr_len = len(arr)
    num_x = arr_len # number holds indexes as they get updated during manipulation
    index_diff = arr[arr_len - (num_x - 1)] - arr[(arr_len - num_x)]

    while True:
        #find the difference beween the adjacent numbers in the sorted array
        current_diff = arr[arr_len - (num_x - 1)] - arr[(arr_len - num_x)]

        if abs(current_diff) < abs(index_diff):
            index_diff = current_diff
            new_array.clear()
            new_array.append(arr[arr_len - num_x])
            new_array.append(arr[arr_len - (num_x - 1)])

        elif abs(current_diff) == abs(index_diff):
            index_diff = current_diff
            new_array.append(arr[arr_len - num_x])
            new_array.append(arr[arr_len - (num_x - 1)])

        num_x -= 1

        if num_x == 1:
            break

    return new_array



my_array = [6, 9, 10, 7, 2, 21, 43, 8, 1]
print(closest_number(my_array))
