#encoding: utf-8
import md5

best_solution = -1
best_pass = None

def main():
    input_file = './input2.txt'

    with open(input_file) as f:
        first_row = f.read()
    
    def generate_row(input_row):
        output_row = ''
        for i, x in enumerate(input_row):
            l = input_row[i - 1] if i > 0 else '.'
            m = x
            r = input_row[i + 1] if i < len(input_row) - 1 else '.'
            
            is_trap = False
            is_trap = is_trap or (l, m, r) == ('^', '^', '.')
            is_trap = is_trap or (l, m, r) == ('.', '^', '^')
            is_trap = is_trap or (l, m, r) == ('^', '.', '.')
            is_trap = is_trap or (l, m, r) == ('.', '.', '^')
            output_row += '^' if is_trap else '.'
        return output_row
    
    last_row = first_row
    n_rows = 400000
    safe_rows = len([x for x in ''.join(last_row) if x == '.'])

    for i in range(n_rows - 1):
        last_row = generate_row(last_row)
        safe_rows += len([x for x in ''.join(last_row) if x == '.'])
    print safe_rows

    



            



            


if __name__ == '__main__':
    main()