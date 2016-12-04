#encoding: utf-8
import re

def main():
    input_file = './input.txt'

    pattern = re.compile(r'\s*(\d+)\s+(\d+)\s+(\d+)')
    with open(input_file) as f:
        triangles = pattern.findall(f.read())
    
    count = 0
    for t in triangles:
        t = sorted([int(x) for x in t])
        count += 1 if t[0] + t[1] > t[2] else 0
    print count


if __name__ == '__main__':
    main()