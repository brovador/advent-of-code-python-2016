#encoding: utf-8
import re

def main():
    input_file = './input.txt'

    with open(input_file) as i:
        instructions = i.read().split('\n')

    input_str = 'abcdefgh'
    input_str = list(input_str)

    def op_swap_position(op_match, input_str):
        output_str = [x for x in input_str]
        pos0, pos1 = [int(x) for x in op_match.groups()]
        output_str[pos0], output_str[pos1] = input_str[pos1], input_str[pos0]
        return output_str

    def op_swap_letter(op_match, input_str):
        output_str = [x for x in input_str]
        letter0, letter1 = op_match.groups()
        pos0, pos1 = input_str.index(letter0), input_str.index(letter1)
        output_str[pos0], output_str[pos1] = input_str[pos1], input_str[pos0]
        return output_str

    def op_rotate(op_match, input_str):
        output_str = [x for x in input_str]
        direction, positions = op_match.groups()[0], int(op_match.groups()[1])
        positions = positions % len(input_str)
        if direction == 'left':
            output_str = input_str[positions:] + input_str[:positions]
        else:
            output_str = input_str[-positions:] + input_str[:-positions]
        return output_str

    def op_rotate_based(op_match, input_str):
        output_str = [x for x in input_str]
        letter = op_match.groups()[0]
        letter_idx = input_str.index(letter)
        positions = letter_idx + 1 + (1 if letter_idx >= 4 else 0)
        positions = positions % len(input_str)
        output_str = input_str[-positions:] + input_str[:-positions]
        return output_str

    def op_reverse(op_match, input_str):
        output_str = [x for x in input_str]
        pos0, pos1 = [int(x) for x in op_match.groups()]
        output_str = input_str[0:pos0] + input_str[pos0:pos1 + 1][::-1] + input_str[pos1 + 1:]
        return output_str

    def op_move(op_match, input_str):
        output_str = [x for x in input_str]
        pos0, pos1 = [int(x) for x in op_match.groups()]
        letter = output_str[pos0]
        del output_str[pos0]
        output_str.insert(pos1, letter)
        return output_str

    operations = {
        r'swap position (\d+) with position (\d+)' : op_swap_position,
        r'swap letter (\w+) with letter (\w+)' : op_swap_letter,
        r'rotate (left|right) (\d+) steps?' : op_rotate,
        r'rotate based on position of letter (\w+)' : op_rotate_based,
        r'reverse positions (\d+) through (\d+)' : op_reverse,
        r'move position (\d+) to position (\d+)' : op_move,
    }

    for instruction in instructions:
        match = None
        for op_pattern, op_func in operations.iteritems():
            match = re.match(op_pattern, instruction)
            if match:
                input_str = op_func(match, input_str)
                break
    print ''.join(input_str)

if __name__ == '__main__':
    main()
