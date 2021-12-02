with open('aoc2021-day2input.txt') as input:
    data = input.readlines()
    data = [line.strip() for line in data]

def part1_solver(data):
    horizontal, depth = 0,0
    for line in data:
        command = line.split()[0]
        increment = int(line.split()[1])
        if command == 'forward':
            horizontal += increment
        elif command == 'down':
            depth += increment
        elif command == 'up':
            depth -= increment
    return horizontal * depth

#part2
def part2_solver(data):
    horizontal,depth,aim = 0,0,0
    for line in data:
        command = line.split()[0]
        increment = int(line.split()[1])
        if command == 'forward':
            horizontal += increment
            depth += (increment * aim)
        elif command == 'down':
            aim += increment
        elif command == 'up':
            aim -= increment
    return horizontal * depth

print(part2_solver(data))