
def check_prime_subtraction(input_list):
    deff = input_list[0] - input_list[1]
    if deff > 1:
        return 'YES'
    else:
        return 'NO'

inputs = []
inputs_num = int(input())

while inputs_num > 0:
    input_data = input().split(' ')
    input_list = []
    for i in input_data:
        input_list.append(int(i))
    inputs.append(input_list)
    inputs_num -= 1

for i in inputs:
    print(check_prime_subtraction(i))
