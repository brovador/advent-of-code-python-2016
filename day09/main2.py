#encoding: utf-8
import re

def main():
    input_file = './input2.txt'

    with open(input_file) as f:
        instructions = f.read().split('\n')
    
    pattern = re.compile(r'\((\d+)x(\d+)\)')
    count = 0

    def compute_size(s):
        m = pattern.search(s)
        size = len(s)
        if m:
            letters, amount = (int(x) for x in m.groups())
            size = len(s[:m.start()]) + amount * compute_size(s[m.end():m.end() + letters])
            size += compute_size(s[m.end() + letters:])
        return size
    
    for i in instructions:
        print compute_size(i.replace(' ', ''))
    
        


if __name__ == '__main__':
    main()