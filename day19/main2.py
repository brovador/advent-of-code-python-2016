#encoding: utf-8
import md5
import math

best_solution = -1
best_pass = None

def main():
    input_file = './input2.txt'

    with open(input_file) as f:
        n = int(f.read())
    
    elves = [x for x in range(1, n + 1)]

    i = 0
    while len(elves) > 1:
        elf = elves[i]
        next_elf_pos = (i + len(elves) / 2) % len(elves)
        next_elf = elves[next_elf_pos]
        del elves[next_elf_pos]
        i = i + 1 if next_elf_pos > i else i
        i = i % len(elves)
        print elf, next_elf, len(elves)
    print elves[0]

if __name__ == '__main__':
    main()