def load_data():
    with open('input.txt', 'r') as f:
        return [line.strip().split() for line in f]