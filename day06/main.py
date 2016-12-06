#encoding: utf-8
from collections import Counter

def main():
    input_file = './input.txt'

    with open(input_file) as f:
        messages = f.read().split('\n')
    
    m_len = len(messages[0])
    counts = [[] for i in range(m_len)]
    for m in messages:
        map(lambda i: counts[i].append(m[i]), range(m_len))
    counts = [Counter(c) for c in counts]
    print ''.join([c.most_common(1)[0][0] for c in counts])

if __name__ == '__main__':
    main()