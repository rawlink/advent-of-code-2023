#!/usr/bin/env python3

NUMBER_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def load(file):
    with open(file) as f:
        values = [line.strip() for line in f]
    return values

def part1(values):
    '''
    >>> part1(load('test1.txt'))
    142
    '''
    return sum(map(lambda x: (x[0] * 10) + x[-1], map(lambda x: get_digits(x, False), values)))

def part2(values):
    '''
    >>> part2(load('test2.txt'))
    281
    '''
    return sum(map(lambda x: (x[0] * 10) + x[-1], map(lambda x: get_digits(x, True), values)))

def get_digits(input, parse):
    return list(filter(lambda x: x is not None, (map(lambda x: convert(input[x:], parse), range(len(input))))))

def convert(value, parse):
    if value[0].isnumeric():
        return int(value[0])

    if parse:
        for num, word in enumerate(NUMBER_WORDS):
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