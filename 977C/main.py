
def convert_into_int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr

def compute_x(arr, k):
    arr.sort()
    z = k - 1
    x = arr[z]
    if k == 0:
        if len(arr) != 0:
            if arr[0] != 1:
                return 1
            else:
                return -1
    if k != len(arr):
        if arr[k] == arr[z]:
            return -1

    return x


k = int(input().split(' ')[1])
input_data = convert_into_int(input().split(' '))
print(compute_x(input_data, k))
