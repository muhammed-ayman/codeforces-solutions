
def compute_min_product(data_list):
    a = int(data_list[0])
    b = int(data_list[1])
    x = int(data_list[2])
    y = int(data_list[3])
    n = int(data_list[4])

    # The least possible number a can be
    if n >= (a-x):
        a_min = x
    else:
        a_min = a-n

    # The least possible number b can be
    if n >= (b-y):
        b_min = y
    else:
        b_min = b-n

    # Senario 1:
    # The number of subtraction operation left for b
    b_op = n - (a - a_min)

    if b_op >= (b-y):
        t1 = a_min * b_min
    else:
        t1 = a_min * (b-b_op)

    # Senario 2:
    # The number of subtraction operation left for a
    a_op = n - (b - b_min)

    if a_op >= (a-x):
        t2 = b_min * a_min
    else:
        t2 = b_min * (a-a_op)

    # Returning the least product of the two senarios
    if t1 < t2:
        return t1
    else:
        return t2

inputs_n = int(input())
inputs_list = []

while inputs_n > 0:
    input_data = input().split(' ')
    inputs_list.append(input_data)
    inputs_n -= 1

for i in inputs_list:
    print(compute_min_product(i))
