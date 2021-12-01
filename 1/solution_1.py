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

print(f"Total increases: {part_1(load_data())}")
print(f"Total increases: {part_1_zip(load_data())}")