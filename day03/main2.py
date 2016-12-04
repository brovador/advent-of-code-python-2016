#encoding: utf-8
import re

def main():
    input_file = './input2.txt'

    pattern = re.compile(r'\s*(\d+)\s+(\d+)\s+(\d+)')
    with open(input_file) as f:
        triangles = pattern.findall(f.read())
    
    count = 0
    for i in range(0, len(triangles), 3):
        for j in range(3):
            t = sorted([int(triangles[i + k][j]) for k in range(3)])
            count += 1 if t[0] + t[1] > t[2] else 0
    print count


if __name__ == '__main__':
    main()