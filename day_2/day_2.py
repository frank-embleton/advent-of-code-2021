def load_data():
    with open('input.txt', 'r') as f:
        return [line.strip().split() for line in f]

def part_1(data):
    h, d = 0, 0
    for direction, value in load_data():
        if direction == 'forward':
            h += int(value)
        elif direction == 'down':
            d += int(value)
        elif direction == 'up':
            d -= int(value)
    return (h * d)

print(f'Part 1: {part_1(load_data())}')


def part_2(data):
    a, h, d = 0, 0, 0
    for direction, value in data:
        if direction == 'down':
            a += int(value)
        elif direction == 'up':
            a -= int(value)
        elif direction == 'forward':
            h += int(value)
            d += a * int(value)
    return (h * d)

print(f'Part 2: {part_2(load_data())}')