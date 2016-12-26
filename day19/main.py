#encoding: utf-8
import md5

best_solution = -1
best_pass = None

def main():
    input_file = './input.txt'

    with open(input_file) as f:
        n = int(f.read())
    
    elves = [[x, 1] for x in range(1, n + 1)]
    while len(elves) > 1:
        for i in range(len(elves)):
            elf = elves[i]
            if elf[1] == 0: continue
            next_elf = elves[i + 1] if i < len(elves) -1 else elves[0]
            elf[1] += next_elf[1]
            next_elf[1] = 0    
            i = i + 1
        elves = [e for e in elves if e[1] > 0]
    print elves[0][0]





    

    



            



            


if __name__ == '__main__':
    main()