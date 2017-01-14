#encoding: utf-8
import re

def main():
    input_file = './input.txt'

    with open(input_file) as i:
        nodes_info = i.read().split('\n')

    nodes_info = nodes_info[2:]
    nodes = {}
    pattern = re.compile(r'([\/\w-]+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%')
    for node_info in nodes_info:
        match = pattern.match(node_info)
        name = match.groups()[0]
        size, used, avail, percent = [int(x) for x in match.groups()[1:]]
        nodes[name] = [size, used, avail, percent]

    pairs = 0
    for node_a in nodes:
        for node_b in nodes:
            if node_a == node_b:
                continue
            node_data_a = nodes[node_a]
            node_data_b = nodes[node_b]

            is_valid_pair = True
            is_valid_pair = is_valid_pair and node_data_a[1] > 0
            is_valid_pair = is_valid_pair and node_data_a[1] <= node_data_b[2]
            if is_valid_pair:
                pairs += 1
    print pairs



if __name__ == '__main__':
    main()
