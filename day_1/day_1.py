def load_data():
    with open('input.txt', 'r') as f:
        return [int(line.strip()) for line in f]

def part_1(data):
    prev = None
    increases = 0
    for reading in data:
        if prev == None:
            ...
        elif reading > prev:
            increases += 1
        prev = reading
    return increases

def part_1_zip(data):
    return sum([x < y for x, y in zip(data, data[1:])])

def part_2(data):
    prev = sum(data[:3])
    increases = 0
    for i, _ in enumerate(data[1:], 1):
        window_sum = sum(data[i:i+3])
        if window_sum > prev:
            increases += 1
        prev = window_sum
    return increases

print(f"Part 1: {part_1(load_data())}")
print(f"Part 1 (zip): {part_1_zip(load_data())}")

print(f"Part 2: {part_2(load_data())}")
