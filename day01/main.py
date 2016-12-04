#encoding: utf-8
import sys
import re
import operator

def main():
    input_file = './input.txt'

    pattern = re.compile(r'([RL])(\d+)')
    with open(input_file, 'r') as f:
        instructions = [(m[0], int(m[1])) for m in pattern.findall(f.read())]
    
    pos = (0, 0)
    d = 0 #Direction: 0: North, 1: East, 2: South, 3: West
    d_inc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for (direction, blocks) in instructions:
        d = (d + (1 if direction == 'R' else -1)) % 4
        increment = tuple(x * blocks for x in d_inc[d])
        pos = tuple(map(operator.add, pos, increment))
    print sum([abs(x) for x in pos])
        
        



if __name__ == '__main__':
    main()