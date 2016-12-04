#encoding: utf-8
from collections import Counter, deque
import re
import string

ROOM_NAME = 0
SECTOR_ID = 1
CHECKSUM = 2

def main():
    input_file = './input2.txt'

    pattern = re.compile(r'([\w-]*)-(\d+)\[(\w+)\]')
    with open(input_file) as f:
        rooms = pattern.findall(f.read())
    
    def comparer(x, y):
            return -1 if x[1] > y[1] or (x[1] == y[1] and x[0] < y[0]) else 1
    
    alphabet = string.lowercase
    for r in rooms:
        r = (r[0], int(r[1]), r[2])
        c = Counter(r[ROOM_NAME].replace('-', ''))
        checksum = ''.join([x[0] for x in sorted(c.most_common(), cmp = comparer)])[:5]
        
        if checksum != r[CHECKSUM]:
            continue
        
        d = deque(alphabet)
        d.rotate(-r[SECTOR_ID])
        trans_tab = string.maketrans(alphabet, ''.join(d))
        room_name = r[ROOM_NAME].translate(trans_tab).replace('-', ' ')
        
        if room_name == 'northpole object storage':
            print r[SECTOR_ID]
            break
        
    


if __name__ == '__main__':
    main()