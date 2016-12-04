#encoding: utf-8
from collections import Counter
import re

def main():
    input_file = './input.txt'

    pattern = re.compile(r'([\w-]*)-(\d+)\[(\w+)\]')
    with open(input_file) as f:
        rooms = pattern.findall(f.read())
    
    def comparer(x, y):
            return -1 if x[1] > y[1] or (x[1] == y[1] and x[0] < y[0]) else 1
    
    ids_sum = 0
    for r in rooms:
        c = Counter(r[0].replace('-', ''))
        checksum = ''.join([x[0] for x in sorted(c.most_common(), cmp = comparer)])[:5]
        ids_sum += int(r[1]) if checksum == r[2] else 0
    print ids_sum


if __name__ == '__main__':
    main()