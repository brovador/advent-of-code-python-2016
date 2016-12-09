#encoding: utf-8

def main():
    input_file = './input.txt'

    with open(input_file) as f:
        ips = f.read().split('\n')
    
    tls_count = 0
    for ip in ips:
        tls_supported = False
        brackets_open = False
        for i, c in enumerate(ip[:-2]):
            if c in '[]':
                brackets_open = c == '['
                continue
            if i == 0:
                continue

            if ip[i - 1:i + 1] == ip[i + 1:i + 3][::-1] and ip[i - 1] != ip[i]:
                if brackets_open:
                    tls_supported = False
                    break
                else:
                    tls_supported = True
        tls_count += 1 if tls_supported else 0
    print tls_count
            


if __name__ == '__main__':
    main()