
def who_wins(play_str):

    lose = 0
    counter = 1

    while counter > 0:
        if (lose == 1) or (len(play_str) == 0):
            break
        for i in range(len(play_str)):
            if i == (len(play_str) - 1):
                lose = 1
                counter += 1
                continue
            if play_str[i] != play_str[i+1]:
                play_str = play_str[:i] + play_str[i+2:]
                break
        counter += 1

    if (counter%2 == 0):
        return 'DA'
    else:
        return 'NET'


inputs_list = []
inputs_num = int(input())

while inputs_num > 0:
    input_data = input()
    inputs_list.append(input_data)
    inputs_num -= 1

for i in inputs_list:
    print(who_wins(i))
