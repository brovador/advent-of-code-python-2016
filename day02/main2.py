#encoding: utf-8
import operator

def main():
    input_file = './input2.txt'

    with open(input_file) as f:
        instructions = [list(s) for s in f.read().split('\n')]
    
    pos = (0, 2)
    pad_nums = [
        '  1  ',
        ' 234 ',
        '56789',
        ' ABC ',
        '  D  ',
    ]
    pad_size = len(pad_nums)
    movements = {
        'L' : (-1, 0),
        'R' : (1, 0),
        'U' : (0, -1),
        'D' : (0, 1), 
    }
    seq = ''

    def pad_num(pos):
        return pad_nums[pos[1]][pos[0]]
    
    for i in instructions:
        for s in i:
            new_pos = tuple(map(operator.add, pos, movements[s]))
            new_pos = tuple(map(lambda x: max(0, min(x, pad_size - 1)), new_pos))
            pos = new_pos if pad_num(new_pos) != ' ' else pos 
        seq += pad_num(pos)
    print seq

if __name__ == '__main__':
    main()