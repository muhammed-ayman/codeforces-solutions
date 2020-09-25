
def compute_exchange_num(n, cubes_vol_list):
    for i in range(len(cubes_vol_list)):
        if i+1 != len(cubes_vol_list):
            if int(cubes_vol_list[i]) <= int(cubes_vol_list[i+1]):
                return 'YES'

    return 'NO'

inputs_num = int(input())
inputs_cubes_num = []
inputs_list = []

while inputs_num > 0:
    cubes_num = int(input())
    cubes_vol = input().split(' ')
    inputs_cubes_num.append(cubes_num)
    inputs_list.append(cubes_vol)
    inputs_num -= 1

for i in range(len(inputs_list)):
    print(compute_exchange_num(inputs_cubes_num[i], inputs_list[i]))
