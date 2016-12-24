#encoding: utf-8
import md5

best_solution = -1
best_pass = None

def main():
    input_file = './input.txt'

    with open(input_file) as f:
        passcode = f.read()
    
    positions_history = []
    position = (0, 0)
    destination = (3, 3)
    size = (4, 4)

    def calculate_moves(position, passcode, steps):
        global best_solution
        global best_pass
        m = md5.new()
        m.update(passcode)
        m = m.hexdigest()

        key = position + [m[:4], ]
        if key  in positions_history:
            return
        positions_history.append(key)
        
        candidates = []
        if m[0] in 'bcdef' and position[1] > 0: 
            candidates.append('U')
        if m[1] in 'bcdef' and position[1] < size[1] - 1: 
            candidates.append('D')
        if m[2] in 'bcdef' and position[0] > 0: 
            candidates.append('L')
        if m[3] in 'bcdef' and position[0] < size[0] - 1: 
            candidates.append('R')
        
        for c in candidates:
            
            new_position = list(position)
            new_steps = steps + 1
            new_passcode = passcode + c
            
            if c == 'L': new_position[0] = position[0] - 1
            elif c == 'R': new_position[0] = position[0] + 1
            elif c == 'U': new_position[1] = position[1] - 1
            elif c == 'D': new_position[1] = position[1] + 1
            
            if new_position == list(destination):
                if best_solution == -1 or new_steps < best_solution:
                    best_solution = new_steps
                    best_pass = new_passcode
                break
            else:
                calculate_moves(new_position, new_passcode, new_steps)
    
    calculate_moves(list(position), passcode, 0)
    print best_pass.replace(passcode, '')


            



            


if __name__ == '__main__':
    main()