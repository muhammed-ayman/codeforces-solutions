
def convert_into_int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr

def compute_longest_subarr(data_arr, undesired):
    total = 0
    length = len(data_arr)
    for i in data_arr:
        total += i
    if (total%undesired) > 0:
        return length

    x = 0
    for i in range(len(data_arr)):
        if data_arr[i]%undesired == 0:
            length -= 1
        else:
            x = i
    if length == 0:
        return -1
    else:
        if x >= (len(data_arr)-1-x):
            return x
        else:
            return (len(data_arr)-1-x)


cases_num = int(input())

undesired_nums = []
inputs_data = []

for i in range(cases_num):
    undesired_input = int(input().split(' ')[1])
    input_data = input().split(' ')
    input_data = convert_into_int(input_data)
    undesired_nums.append(undesired_input)
    inputs_data.append(input_data)

for x in range(len(inputs_data)):
    x1 = (compute_longest_subarr(inputs_data[x], undesired_nums[x]))
    arr_reversed = inputs_data[x]
    arr_reversed.reverse()
    x2 = (compute_longest_subarr(arr_reversed, undesired_nums[x]))
    if x1 > x2:
        print(x1)
    else:
        print(x2)
