
import string
letters_list = list(string.ascii_uppercase)


# EX: BC23 -> R23C55
def system_one(cell_info):
    for i in range(len(cell_info)):
        try:
            row = int(cell_info[i:])
            column = cell_info[:i]
            break
        except:
            pass

    column_num = 0
    for i in range(len(column)-1):
        column_num += (26**(i+1))
        column_num += (letters_list.index(column[i])) * (26**(len(column)-(i+1)))

    column_num += letters_list.index(column[len(column)-1])+1
    return ('R'+str(row)+'C'+str(column_num))

# EX: R23C55 -> BC23
def system_two(cell_info):
    for i in range(len(cell_info)):
        if cell_info[i] == 'C':
            column_num = int(cell_info[i+1:])
            row_num = cell_info[1:i]
            break

    column = ''
    while column_num > 0:
        letter_index = (column_num%26)-1
        column = letters_list[letter_index] + column
        column_num = int((column_num-1)/26)
    return (column + row_num)

n = int(input())
inputs_list = []

while n > 0:
    data_input = input()
    inputs_list.append(data_input)
    n -= 1

for i in inputs_list:
    if i[0] == "R":
        try:
            int(i[1])
            if 'C' in i:
                print(system_two(i))
            else:
                print(system_one(i))
        except:
            print(system_one(i))
    else:
        print(system_one(i))
