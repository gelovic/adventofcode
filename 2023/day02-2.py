import re

def find_fewest(line):
    game = re.findall(r'(\d{1,}).(red|green|blue)', line)
    cubes = {}
    for number, color in game:
        cubes[color] = max(cubes.get(color, 0), int(number)) 
    return cubes['red'] * cubes['green'] * cubes['blue']

with open('day02-input', 'r') as data:
    total = sum(find_fewest(line) for line in data.readlines())
    print(total)