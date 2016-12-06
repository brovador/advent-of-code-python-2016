#encoding: utf-8
from __future__ import print_function
import md5

def main():
    input_file = './input.txt'

    with open(input_file) as f:
        door_id = f.read()
    i = 0
    r = ''
    while (len(r) < 8):
        m = md5.new()
        m.update(door_id + str(i))
        hd = m.hexdigest()
        print(r + hd[5], end = '\r')
        if hd[0:5] == '00000':
            r += hd[5]
        i += 1
    print(r)


if __name__ == '__main__':
    main()