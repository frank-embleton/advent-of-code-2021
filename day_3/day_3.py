def load_data():
    with open('input.txt', 'r') as f:
        return [line.strip() for line in f]


def find_most_common(data, idx):
    r = [0, 0]
    for line in data:
        r[int(line[idx])] += 1
    return '0' if r[0] > r[1] else '1'


def part_1(data):
    result = []
    for idx in range(12):
        result.append(find_most_common(data, idx))
    gamma = ''.join(result)
    epsilon = ''.join(['1' if x == '0' else '0' for x in result])
    return int(gamma, 2) * int(epsilon, 2)


print(f'Part 1: {part_1(load_data())}')


def find_least_common(data, idx):
    r = [0, 0]
    for line in data:
        r[int(line[idx])] += 1
    return '0' if r[0] < r[1] else '1'


def oxygen(data, idx=0):
    most_common = find_most_common(data, idx)
    data = [line for line in data if line[idx] == most_common]
    if len(data) != 1:
        return oxygen(data, idx+1)
    return int(data[0], 2)


def co2(data, idx=0):
    least_common = find_least_common(data, idx)
    data = [line for line in data if line[idx] == least_common]
    if len(data) != 1:
        return co2(data, idx+1)
    return int(data[0], 2)

print(f'Part 2: {oxygen(load_data()) * co2(load_data())}')