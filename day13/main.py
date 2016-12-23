#encoding: utf-8

best_solution = 10000000
n = 0

def main():
    global n
    input_file = './input.txt'

    with open(input_file) as f:
        n = int(f.read())
    
    pos_history = {}

    
    def compute_cell(x, y, n):
        tmp = x * x + 3 * x + 2 * x * y + y + y * y
        tmp += n
        tmp = bin(tmp).replace('0b', '')
        tmp = sum([int(t) == 1 for t in tmp])
        return '.' if tmp % 2 == 0 else '#'

    def distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    

    def find_solution(current_pos, end_pos, current_steps):
        global best_solution
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
            valid = valid and compute_cell(c[0], c[1], n) == '.'
            valid = valid and pos_history.get(str(c), n) >= current_steps
            return valid

        candidates = [c for c in candidates if valid_candidate(c)]
        candidates.sort(key = lambda x: distance(x, end_pos))
        for c in candidates:
            if c == end_pos:
                if current_steps + 1 < best_solution:
                    best_solution = current_steps + 1
                break
            pos_history[str(c)] = current_steps + 1
            find_solution(c, end_pos, current_steps + 1)
            
    pos = (1, 1)
    end_pos = (31,39)
    steps = 0
    find_solution(pos, end_pos, steps)
    print best_solution



            


if __name__ == '__main__':
    main()