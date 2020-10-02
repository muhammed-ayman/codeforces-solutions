
def compute_minimum_distance(input_arr):
    for i in range(len(input_arr)):
        input_arr[i] = int(input_arr[i])
    input_arr.sort()
    if (input_arr[0] == input_arr[1]) and (input_arr[1] == input_arr[2]):
        return 0

    if ((input_arr[2] - input_arr[1]) >= 2) and (input_arr[0] == input_arr[1]):
        input_arr[2] -= 2
        res = abs(input_arr[2] - input_arr[1]) + abs(input_arr[1] - input_arr[0]) + abs(input_arr[2] - input_arr[0])
        return res
    if ((input_arr[1] - input_arr[0]) >= 2) and (input_arr[2] == input_arr[1]):
        input_arr[0] += 2
        res = abs(input_arr[2] - input_arr[1]) + abs(input_arr[1] - input_arr[0]) + abs(input_arr[2] - input_arr[0])
        return res

    if input_arr[0] != input_arr[1]:
        input_arr[0] += 1
    if input_arr[1] != input_arr[2]:
        input_arr[2] -= 1

    res = abs(input_arr[2] - input_arr[1]) + abs(input_arr[1] - input_arr[0]) + abs(input_arr[2] - input_arr[0])
    return res


inputs = []
inputs_num = int(input())

while inputs_num > 0:
    input_data = input().split(' ')
    inputs.append(input_data)
    inputs_num -= 1

for i in inputs:
    print(compute_minimum_distance(i))
