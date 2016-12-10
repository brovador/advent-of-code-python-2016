#encoding: utf-8
import re

def main():
    input_file = './input.txt'

    with open(input_file) as f:
        instructions = f.read().split('\n')
    
    screen_size = (50, 6)
    screen = [list('.' * screen_size[0]) for i in range(screen_size[1])]

    def print_screen():
        for l in screen:
            print ''.join(l)

    def rect_command(m):
        w, h = (int(x) for x in m.groups())
        for i in range(h):
            for j in range(w):
                screen[i][j] = '#' 

    def rotate_command(m):
        command, coord, amount = m.groups()
        coord, amount = int(coord), int(amount)
        if command == 'row':
            amount = amount % screen_size[0]
            screen[coord] = screen[coord][-amount:] + screen[coord][:-amount]
        else:
            s = []
            amount = amount % screen_size[1]
            for j in range(screen_size[0]):
                s.append([screen[i][j] for i in range(screen_size[1])])
            s[coord] = s[coord][-amount:] + s[coord][:-amount]
            for i in range(screen_size[1]):
                screen[i] = [s[j][i] for j in range(screen_size[0])]
    
    commands = {
        'rect' : r'rect (\d+)x(\d+)',
        'rotate' : r'rotate (column|row) \w=(\d+) by (\d+)',
    }
    
    for i in instructions:
        for command, pattern in commands.iteritems():
            m = re.match(pattern, i)
            if not m: 
                continue
            if command == 'rect':
                rect_command(m)
            elif command == 'rotate':
                rotate_command(m)
            #print i
    print_screen()
    print sum([sum(map(lambda e: e == '#', s)) for s in screen])
    


if __name__ == '__main__':
    main()