#encoding: utf-8

def main():
    input_file = './input2.txt'

    with open(input_file) as f:
        ips = f.read().split('\n')
    
    ssl_count = 0
    for ip in ips:
        brackets_open = False
        sn_sequences = []
        hn_sequences = []
        tmp = ''
        for c in ip:
            if c in '[]':
                brackets_open = c == '['
                if not brackets_open:
                    hn_sequences.append(tmp)
                else:
                    sn_sequences.append(tmp)
                tmp = ''
            else:
                tmp += c
        if tmp != '':
            sn_sequences.append(tmp)
        
        ssl_supported = False
        for seq in sn_sequences:
            for i in range(len(seq) - 2):
                if seq[i] == seq[i + 1] or seq[i] != seq[i + 2]:
                    continue
                s = seq[i + 1] + seq[i] + seq[i + 1]
                ssl_supported = any([s in x for x in hn_sequences])
                if ssl_supported:
                    break
            if ssl_supported:
                break
        ssl_count += 1 if ssl_supported else 0
    print ssl_count
            


if __name__ == '__main__':
    main()