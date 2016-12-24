#encoding: utf-8

def main():
    input_file = './input2.txt'
    disc_length = 35651584

    with open(input_file) as f:
        initial_state = f.read()
    
    def fill_data(a):
        b = a + '0' + ''.join(['0' if x == '1' else '1' for x in a[::-1]])
        if len(b) < disc_length:
            b = fill_data(b)
        return b[:disc_length]
    
    def generate_checksum(data):
        s = ''.join(['1' if data[i] == data[i + 1] else '0' for i in range(0, len(data), 2)])
        if len(s) % 2 == 0:
            s = generate_checksum(s)
        return s

    
    data = fill_data(initial_state)
    checksum = generate_checksum(data)
    print checksum



            



            


if __name__ == '__main__':
    main()