with open('aoc2021-day3input.txt') as input:
    data = input.readlines()
    data = [line.strip() for line in data]

#part 1

def gamma_finder(data):
    #lines are 12 chars long
    line_index = 0
    final_value = ''
    while line_index < 12:       
        ones = 0
        zeros = 0
        for line in data:
            if line[line_index] == '1':
                ones += 1
            elif line[line_index] == '0':
                zeros += 1
        if ones > zeros:
            final_value = final_value + '1'
        else:
            final_value = final_value + '0'
        line_index += 1
        ones, zeros = 0,0
    return int(final_value,2)

def epsilon_finder(data):
    #lines are 12 chars long
    line_index = 0
    final_value = ''
    while line_index < 12:       
        ones = 0
        zeros = 0
        for line in data:
            if line[line_index] == '1':
                ones += 1
            elif line[line_index] == '0':
                zeros += 1
        #this is inverted vs gamma
        if ones > zeros:
            final_value = final_value + '0'
        else:
            final_value = final_value + '1'
        line_index += 1
        ones, zeros = 0,0
    return int(final_value,2)

#print(gamma_finder(data)*(epsilon_finder(data)))

#part 2

def oxygen_generator_finder(data:list):
    #lines are 12 chars long
    max_len = len(data[0])

    for i in range(max_len):
        zeros = 0
        ones = 0
        for line in data:
            if line[i] == '1':
                ones += 1
            elif line[i] == '0':
                zeros += 1
        if ones >= zeros:
            data = [line for line in data if line[i] == '1']
        else:
            data = [line for line in data if line[i] == '0']
    return int(data[0],2)

#print(oxygen_generator_finder(data))

def co2_scrubber_rating(data:list):
    max_len = len(data[0])
    for i in range(max_len):
        zeros = 0
        ones = 0
        for line in data:
            if line[i] == '1':
                ones += 1
            elif line[i] == '0':
                zeros += 1
        if zeros <= ones:
            data = [line for line in data if line[i] == '0']
        else:
            data = [line for line in data if line[i] == '1']
        if len(data) == 1:
            return int(data[0],2)


#pt2 answer
print(oxygen_generator_finder(data) * co2_scrubber_rating(data))