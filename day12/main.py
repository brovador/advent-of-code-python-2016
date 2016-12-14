#encoding: utf-8
import re

ic = 0
registers = {
    'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0
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
        y = int(y)
        ic += y - 1 if x else 0
    
    operations = {
        r'cpy (.+) (.+)' : op_copy,
        r'inc (.+)' : op_inc, 
        r'dec (.+)' : op_dec,
        r'jnz (.+) (.+)' : op_jnz,  
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