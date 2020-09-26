
def determine_danger(string):
    d = 0
    for i in range(len(string)):
        if d == 6:
            return 'YES'
        if i+1 != len(string):
            if string[i] == string[i+1]:
                d += 1
            else:
                d = 0

    return 'NO'


players_string = input()
print(determine_danger(players_string))
