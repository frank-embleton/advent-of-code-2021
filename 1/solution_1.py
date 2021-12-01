with open('input.txt', 'r') as f:
    data = f.read().splitlines()

data = [int(x) for x in data]

prev = data[0]
increases = 0
for reading in data[1:]:
    if reading > prev:
        increases += 1
    prev = reading

print(f"Total increases: {increases}")