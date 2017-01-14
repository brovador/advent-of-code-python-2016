#encoding: utf-8
import re

ic = 0
registers = {
    'a' : 7, 'b' : 0, 'c' : 0, 'd' : 0
}

def main():
    global ic
    input_file = './input.txt'

    with open(input_file) as f:
        instructions = f.read().split('\n')
    
    def op_copy(m):
        x, y = m.groups()
        registers[y] = int(x) if not x in 'abcd' else registers[x]
    
    def op_inc(m):
        registers[m.groups()[0]] += 1
    
    def op_dec(m):
        registers[m.groups()[0]] -= 1
    
    def op_jnz(m):
        global ic
        x, y = m.groups()
        x = int(x) if not x in 'abcd' else registers[x]
        y = int(y) if not y in 'abcd' else registers[y]
        ic += y - 1 if x else 0
    
    def op_tgl(m):
        global ic
        inc = m.groups()[0]
        inc = int(inc) if not inc in 'abcd' else registers[inc]
        if ic + inc < len(instructions) - 1:
            instruction = instructions[ic + inc].split(' ')
            if len(instruction) <= 2:
                instruction[0] = 'dec' if instruction[0] == 'inc' else 'inc'
            else:
                instruction[0] = 'cpy' if instruction[0] == 'jnz' else 'jnz'
            instructions[ic + inc] = ' '.join(instruction)
    
    operations = {
        r'cpy (.+) (\w+)' : op_copy,
        r'inc (.+)' : op_inc, 
        r'dec (.+)' : op_dec,
        r'jnz (.+) (.+)' : op_jnz,
        r'tgl (.+)' : op_tgl,  
    }

    while ic < len(instructions):
        i = instructions[ic]
        for pattern, operation in operations.iteritems():
            m = re.match(pattern, i)
            if m:
                operation(m)
        ic += 1
    print registers['a']

if __name__ == '__main__':
    main()