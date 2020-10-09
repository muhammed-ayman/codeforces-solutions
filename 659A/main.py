from math import ceil

def compute_last_entrance(n, a, b):
    if b == 0 or n == 1 or n == b:
        return a

    x = a + b

    if x > n:
        y = ceil(x/n)
        x -= y*n
        if x <= 0:
            x += n
        return x
    else:
        if x > 0:
            return x
        if x == 0:
            return n
        y = ceil(abs(x)/n)
        x += n*y
        if x == 0:
            x += n
        return x

inputs = input().split(' ')
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])

print(compute_last_entrance(inputs[0], inputs[1], inputs[2]))
