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
        y = int(y) if not y in 'abcd' else registers[y]
        if x != 0:
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
        
    def op_out(m):
        x = m.groups()[0]
        x = int(x) if x not in 'abcd' else registers[x]
        out_signal.append(x)

    out_signal = []
    operations = {
        r'cpy (.+) (\w+)' : op_copy,
        r'inc (.+)' : op_inc, 
        r'dec (.+)' : op_dec,
        r'jnz (.+) (.+)' : op_jnz,
        r'tgl (.+)' : op_tgl, 
        r'out (.+)' : op_out,
    }

    a_value = -1
    while True:
        a_value += 1
        out_signal = []
        ic = 0
        registers = {
            'a' : a_value, 'b' : 0, 'c' : 0, 'd' : 0
        }
        print 'testing a:', a_value
        while ic < len(instructions):
            i = instructions[ic]
            for pattern, operation in operations.iteritems():
                m = re.match(pattern, i)
                if m:
                    operation(m)
            ic += 1
            is_valid_output = all([x == 0 if i % 2 == 0 else x == 1 for i,x in enumerate(out_signal)])
            if not is_valid_output:
                print 'not valid signal: ', out_signal
                break
        if len(out_signal) > 20:
            break
    print a_value, out_signal

if __name__ == '__main__':
    main()