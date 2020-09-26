
def compute_weight_division(weight):
    if (weight%2 == 0) and (weight != 2):
        return 'YES'

    return 'NO'

weight = int(input())
print(compute_weight_division(weight))
