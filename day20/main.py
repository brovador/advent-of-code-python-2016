#encoding: utf-8

def main():
    input_file = './input.txt'

    with open(input_file) as i:
        ranges = i.read().split('\n')

    ranges = [[int(x) for x in r.split('-')] for r in ranges]
    ranges.sort(key=lambda x: x[0])

    i = 0
    for r in ranges:
        if i < r[0]:
            break
        i = r[1] + 1
    print i

if __name__ == '__main__':
    main()
