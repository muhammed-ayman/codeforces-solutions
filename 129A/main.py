
def compute_ways_number(total, bags_contents):
    x = 0
    if total%2 == 0:
        for i in bags_contents:
            if i%2 == 0:
                x += 1
    else:
        for i in bags_contents:
            if i%2 != 0:
                x += 1
    return x


total = 0
bags_num = int(input())
bags_contents = input().split(' ')

for i in range(len(bags_contents)):
    bags_contents[i] = int(bags_contents[i])
    total += bags_contents[i]

print(compute_ways_number(total, bags_contents))
