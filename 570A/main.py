
def determine_winner(cities_data):
    cities_winners = []
    winners = []
    for i in range(len(cities_data)):
        max_votes = 0
        for j in range(len(cities_data[i])):
            if cities_data[i][j] >= max_votes:
                max_votes = cities_data[i][j]
        for z in range(len(cities_data[i])):
            if cities_data[i][z] == max_votes:
                winners.append(z)
                break

    winners.sort()
    element = 0
    count = 0
    for i in range(len(winners)):
        temp_element = winners[i]
        temp_count = 0
        for j in range(len(winners)):
            if winners[j] == temp_element:
                temp_count += 1
        if temp_count > count:
            count = temp_count
            element = temp_element

    return element+1

def convert_into_int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr

inputs_nums = input().split(' ')
inputs_nums = convert_into_int(inputs_nums)

inputs_data = []

for i in range(inputs_nums[1]):
    input_data = input().split(' ')
    input_data = convert_into_int(input_data)
    inputs_data.append(input_data)

print(determine_winner(inputs_data))
