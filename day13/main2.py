#encoding: utf-8

max_steps = 50

def main():
    global n
    input_file = './input2.txt'

    with open(input_file) as f:
        n = int(f.read())
    
    pos_history = {}
    pos_found = set([])

    
    def compute_cell(x, y, n):
        tmp = x * x + 3 * x + 2 * x * y + y + y * y
        tmp += n
        tmp = bin(tmp).replace('0b', '')
        tmp = sum([int(t) == 1 for t in tmp])
        return '.' if tmp % 2 == 0 else '#'

    def distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    

    def find_solution(current_pos, current_steps):
        global max_steps

        pos_history[str(current_pos)] = current_steps
        pos_found.add(current_pos)

        candidates = [
            (current_pos[0] - 1, current_pos[1]),
            (current_pos[0] + 1, current_pos[1]),
            (current_pos[0], current_pos[1] - 1),
            (current_pos[0], current_pos[1] + 1),
        ]

        def valid_candidate(c):
            global n
            valid = True
            valid = valid and c[0] >= 0 and c[1] >= 0
            valid = valid and pos_history.get(str(c), 10000) >= current_steps
            valid = valid and compute_cell(c[0], c[1], n) == '.'
            return valid

        candidates = [c for c in candidates if valid_candidate(c)]
        for c in candidates:
            if current_steps < max_steps:
                find_solution(c, current_steps + 1)
            
    pos = (1, 1)
    steps = 0
    find_solution(pos, steps)
    print len(pos_found)



            


if __name__ == '__main__':
    main()