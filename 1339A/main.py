
inputs_list = []
inputs_num = int(input())

while inputs_num > 0:
    input_data = input()
    inputs_list.append(input_data)
    inputs_num -= 1

for i in inputs_list:
    print(i)
