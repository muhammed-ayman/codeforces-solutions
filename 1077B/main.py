
def compute_k(flats):
    x = []
    k = 0
    for i in range(len(flats)):
        if ((i != 0) and (i+1 != len(flats))):
            if flats[i] == 0 and flats[i-1] == 1 and flats[i+1] == 1:
                x.append(i)
    k = len(x)
    for i in range(len(x)):
        if i+1 != len(x):
            if x[i]+2 == x[i+1]:
                x[i+1] -= 1
                k -= 1

    return k

flats_num = int(input())
flats_conditions = input().split(' ')

for i in range(len(flats_conditions)):
    flats_conditions[i] = int(flats_conditions[i])

print(compute_k(flats_conditions))
