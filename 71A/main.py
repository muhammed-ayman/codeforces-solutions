

def abbr_word(word):
    if len(word) > 10:
        word = word[0] + str(len(word)-2) + word[len(word)-1]

    return word

inputs_num = int(input())
inputs_list = []

while inputs_num > 0:
    input_data = input()
    inputs_list.append(input_data)
    inputs_num -= 1

for i in inputs_list:
    print(abbr_word(i))
