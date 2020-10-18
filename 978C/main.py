
def solve_cipher(dorms_num, letters_num, rooms, letters):
    total_nums = 0
    for i in rooms:
        total_nums += i
    z = []
    for i in range(len(rooms)):
        if i != 0:
            f = [z[i-1][1],z[i-1][1]+rooms[i]]
        else:
            f = [0, rooms[i]]
        z.append(f)

    ls = 0
    for i in letters:
        for j in range(ls,len(z)):
            if (i >= z[j][0]) and (i <= z[j][1]):
                strs = str(j+1) + " " + str(i-z[j][0])
                ls = j
                print(strs)
                break

def convert_to_int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr


first_line_data = input().split(' ')
second_line_data = input().split(' ')
third_line_data = input().split(' ')

first_line_data = convert_to_int(first_line_data)
rooms = convert_to_int(second_line_data)
letters = convert_to_int(third_line_data)

dorms_num = first_line_data[0]
letters_num = first_line_data[1]

solve_cipher(dorms_num, letters_num, rooms, letters)
