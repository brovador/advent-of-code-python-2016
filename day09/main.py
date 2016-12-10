#encoding: utf-8
import re

def main():
    input_file = './input.txt'

    with open(input_file) as f:
        instructions = f.read().split('\n')
    
    pattern = re.compile(r'\((\d+)x(\d+)\)')
    count = 0
    for i in instructions:
        i = i.replace(' ', '')
        m = pattern.search(i)
        end_idx = 0
        s = ''
        while(m):
            s += i[:m.start()]
            letters, amount = (int(x) for x in m.groups())
            end_idx = m.end() + letters
            s += i[m.end():end_idx] * amount
            i = i[end_idx:]
            m = pattern.search(i)
        s += i
        count += len(s)
    print count
    
        


if __name__ == '__main__':
    main()