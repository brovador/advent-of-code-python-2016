#encoding: utf-8
import operator

def main():
    input_file = './input.txt'

    with open(input_file) as f:
        instructions = [list(s) for s in f.read().split('\n')]
    
    pos = (1, 1)
    pad_size = 3
    movements = {
        'L' : (-1, 0),
        'R' : (1, 0),
        'U' : (0, -1),
        'D' : (0, 1), 
    }
    seq = ''
    for i in instructions:
        for s in i:
            pos = tuple(map(operator.add, pos, movements[s]))
            pos = (max(0, min(pos[0], pad_size - 1)), max(0, min(pos[1], pad_size - 1))) 
        seq += str(pos[1] * pad_size + pos[0] + 1)
    print seq

if __name__ == '__main__':
    main()