#!/usr/bin/env python3
import math

def load(file):
    with open(file) as f:
        lines = [line.strip() for line in f]
        games = {}
        for line in lines:
            [name, content] = line.split(':')
            game = int(name.split(' ')[1])
            draws = [draw.strip() for draw in content.split(';')]
            for draw in draws:
                colors = {color.strip():int(count) for [count, color] in [colorcount.strip().split(' ') for colorcount in draw.split(',')]}
                if game not in games:
                    games[game] = []
                games[game].append(colors)
            
    return games

def part1(drawmaxes, bag):
    '''
    >>> part1(get_drawmaxes(load('test1.txt')), {'red': 12, 'green': 13, 'blue': 14})
    8
    '''
    return sum([game for game, drawmax in drawmaxes.items() if all([drawmax[color] <= bag[color] for color in bag])])

def get_drawmaxes(games):
    return {game:get_drawmax(draws) for game, draws in games.items()}

def get_drawmax(draws):
    drawmax = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        for color, count in draw.items():
            drawmax[color] = max(drawmax[color], count)
    return drawmax

def part2(drawmaxes):
    '''
    >>> part2(get_drawmaxes(load('test1.txt')))
    2286
    '''
    return sum([math.prod(drawmax.values()) for drawmax in drawmaxes.values()])

def main():
    bag = {'red': 12, 'green': 13, 'blue': 14}
    games = load('input.txt')
    drawmaxes = get_drawmaxes(games)

    value = part1(drawmaxes, bag)
    print(f'Part 1: {value}')
    assert value == 3099

    value = part2(drawmaxes)
    print(f'Part 2: {value}')
    assert value == 72970

if __name__ == '__main__':
    main()