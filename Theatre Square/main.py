
import math

inputs_list = input().split(' ')

n = float(inputs_list[0])
m = float(inputs_list[1])
a = float(inputs_list[2])

if n < m:
    n, m = m, n

width = math.ceil(n/a)
height = math.ceil(m/a)
area = width * height

print(area)
