#encoding: utf-8
import re

def main():
    input_file = './input2.txt'

    with open(input_file) as f:
        instructions = f.read().split('\n')
    
    pattern = re.compile('Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).')
    discs = []
    for i in instructions:
        m = pattern.match(i)
        discs.append(tuple([int(x) for x in m.groups()[1:]]))
    discs.append((11, 0))
    
    def compute_position(t, d):
        return (t % d[0] + d[1]) % d[0]
    
    t = 0
    while True:
        if all([compute_position(t + i + 1, d) == 0 for i, d in enumerate(discs)]):
            break
        t += 1
    print t




            



            


if __name__ == '__main__':
    main()