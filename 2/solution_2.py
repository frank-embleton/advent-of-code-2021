with open('input.txt', 'r') as f:
    data = f.read().splitlines()

data = [int(x) for x in data]

prev = sum(data[:3])
increases = 0
for i, _ in enumerate(data[1:], 1):
    window_sum = sum(data[i:i+3])
    if window_sum > prev:
        increases += 1
    prev = window_sum

print(f"Total increases: {increases}")