#!/usr/bin/env python3

NUMBER_WORDS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
}

def load(file):
    with open(file) as f:
        values = [line.strip() for line in f.readlines()]
    return values

def part1(values):
    '''
    >>> part1(load('test1.txt'))
    142
    '''
    calibration = 0
    for value in values:
        digits = list(filter(lambda x: x.isnumeric(), value))
        calibration += int(f'{digits[0]}{digits[-1]}')
    return calibration

def part2(values):
    '''
    >>> part2(load('test2.txt'))
    281
    '''
    calibration = 0
    for value in values:
        first = get_digit(value, False)
        last = get_digit(value, True)
        calibration += int(f'{first}{last}')
    return calibration

def get_digit(value, reverse):
    r = range(len(value) - 1, -1, -1) if reverse else range(len(value))
    for i in r:
        num = convert(value[i:])
        if num is not None:
            return num
    raise Exception('No digit found')

def convert(value):
    if value[0].isnumeric():
        return value[0]
    for word, num in NUMBER_WORDS.items():
        if value.startswith(word):
            return num
    return None

def main():
    values = load('input.txt')
    value = part1(values)
    print(f'Part 1: {value}')
    assert value == 54304

    value = part2(values)
    print(f'Part 2: {value}')
    assert value == 54418

if __name__ == '__main__':
    main()