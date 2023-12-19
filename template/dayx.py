#!/usr/bin/env python3

def load(file):
    with open(file) as f:
        values = [line.strip() for line in f.readlines()]
    return values

def part1(values):
    '''
    >>> part1(load('test1.txt'))
    0
    '''
    return 0

def part2(values):
    '''
    >>> part2(load('test1.txt'))
    0
    '''
    return 0

def main():
    values = load('input.txt')
    value = part1(values)
    print(f'Part 1: {value}')
    assert value == 0

    value = part2(values)
    print(f'Part 2: {value}')
    assert value == 0

if __name__ == '__main__':
    main()