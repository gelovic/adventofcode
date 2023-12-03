import re

with open('day01-input', 'r') as data:
    total = sum(int(numbers[0]+numbers[-1]) for line in data.readlines() if (numbers := re.findall(r'\d', line)))
    print(total)