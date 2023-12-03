import re

def to_number(line):
    numbers = 'one|two|three|four|five|six|seven|eight|nine'
    digits = re.findall(rf'(?=({numbers}|\d))', line)
    values = ''.join(str(numbers.split('|').index(n)+1) if n.isalpha() else n for n in (digits[0], digits[-1]))
    return int(values)

with open('day01-input', 'r') as data:
    total = sum(to_number(line) for line in data.readlines())
    print(total)