
def compute_steps(n, k):
    if k > n:
        return int(k-n)

    steps = 0
    while 1:
        z = (k+n)/2
        if int(z) == z:
            return int(steps)
        else:
            n += 1
            steps += 1


inputs_list = []
inputs_num = int(input())

while inputs_num > 0:
    input_data = input().split(' ')
    inputs_list.append(input_data)
    inputs_num -= 1

for i in inputs_list:
    print(compute_steps(float(i[0]), float(i[1])))
