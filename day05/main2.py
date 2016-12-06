#encoding: utf-8
from __future__ import print_function
import md5

def main():
    input_file = './input2.txt'

    with open(input_file) as f:
        door_id = f.read()
    i = 0
    r = list('________')
    while ('_' in r):
        m = md5.new()
        m.update(door_id + str(i))
        hd = m.hexdigest()
        pos, value = int(hd[5], 16), hd[6]
        if hd[0:5] == '00000' and pos < 8 and r[pos] == '_':
            r[pos] = value
        print(''.join(r), i, end = '\r')
        i += 1
    print(''.join(r))


if __name__ == '__main__':
    main()