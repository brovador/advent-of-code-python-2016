#encoding: utf-8

def main():
    input_file = './input2.txt'

    with open(input_file) as i:
        ranges = i.read().split('\n')

    ranges = [[int(x) for x in r.split('-')] for r in ranges]
    ranges.sort(key=lambda x: x[0])

    max_ip = 4294967295
    count = 0
    ridx = 0
    i = 0
    while i < max_ip and ridx < len(ranges):
        ritem = ranges[ridx]
        if i < ritem[0]:
            count += ritem[0] - i
        #print i, ritem, count
        #raw_input()
        i = max(i, ritem[1] + 1)
        ridx += 1
    if i < max_ip:
        count += max_ip - i
    print count

if __name__ == '__main__':
    main()
