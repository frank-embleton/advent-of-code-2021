from itertools import chain


def load_data():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def create_cards(data):
    cards = {}
    idx = 0
    for line in data[1:]:
        if line == "":
            idx += 1
            cards[idx] = []
        else:
            values = [val for val in line.split(" ") if val != ""]
            cards[idx].append(values)
    return cards


def call_number(number, cards):
    for card in cards:
        for line in cards[card]:
            for idx, val in enumerate(line):
                if val == number:
                    line[idx] = None
    return cards


def return_winning_cards(cards, number):
    win_card = []
    win_idx = []
    for card in cards:
        for line in cards[card]:
            if sum(1 for val in line if val == None) == 5:
                win_card.append((cards[card], number))
                win_idx.append(card)
        for col in range(5):
            if sum(1 for line in cards[card] if line[col] == None) == 5:
                win_card.append((cards[card], number))
                win_idx.append(card)
    for card in win_idx:
        cards.pop(card, None)
    return cards, win_card
    

def part_1(data):
    numbers = data[0].split(",")
    cards = create_cards(data)
    winners = []
    for number in numbers:
        cards = call_number(number, cards)
        cards, win = return_winning_cards(cards, number)
        winners.extend(win)
    card, number = winners[0]  
    card_sum = sum([int(n) for n in chain.from_iterable(card) if n != None])
    return int(number) * card_sum


def part_2(data):
    numbers = data[0].split(",")
    cards = create_cards(data)
    winners = []
    for number in numbers:
        cards = call_number(number, cards)
        cards, win = return_winning_cards(cards, number)
        winners.extend(win)
    card, number = winners[-1]  
    card_sum = sum([int(n) for n in chain.from_iterable(card) if n != None])
    return int(number) * card_sum


print(f'Part 1: {part_1(load_data())}')
print(f'Part 2: {part_2(load_data())}')
