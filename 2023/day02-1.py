import re

cubes = {'red': 12, 'green': 13, 'blue': 14}

def find_games(line):
    game = re.findall(r'(\d{1,}).(red|green|blue)', line)
    valid = all(cubes[color] >= int(number) for number, color in game)
    return int(re.findall(r'(\d{1,}):', line)[0]) if valid else 0

with open('day02-input', 'r') as data:
    total = sum(find_games(line) for line in data.readlines())
    print(total)