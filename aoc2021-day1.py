with open('aoc2021-day1input.txt') as input:
    data = input.readlines()
    data = [int(line.strip()) for line in data]

#part 1
index = data[0]
increases = 0

for line in data[1:]:
    if line > index:
        increases += 1
    index = line

#part 2
def part2_solver(input):
    list_index = 0
    grouped_list = []
    increments = 0
    while list_index < 1998:
        grouped_list.append(input[list_index]+input[list_index+1]+input[list_index+2])
        list_index += 1
    for i in range(len(grouped_list)-1):
        if grouped_list[i+1] > grouped_list[i]:
            increments += 1
    return increments

print(part2_solver(data))
