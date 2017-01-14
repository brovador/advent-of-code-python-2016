#encoding: utf-8
import operator
import itertools

def main():
    input_file = './input2.txt'

    with open(input_file) as i:
        maze_lines = i.read().split('\n')
    
    maze = []
    for line in maze_lines:
        maze.append(list(line))
    w, h = len(maze[0]), len(maze)
    
    positions = {}
    for x in range(w):
        for y in range(h):
            i = maze[y][x]
            if i not in '.#':
                positions[i] = (x, y)
    
    def calculate_distance(maze, ipos, jpos):
        queue = [[ipos]]
        best_distance = -1
        shortests_paths = {}

        def distance(path):
            return abs(path[-1][0] - jpos[0]) + abs(path[-1][1] - jpos[1])

        while len(queue):
            root_node = queue[0]
            queue.remove(root_node)
            #Analyze current node
            last_pos = root_node[-1]
            last_pos_shortest_path = shortests_paths.get(last_pos, -1)
            if last_pos_shortest_path != -1 and last_pos_shortest_path <= len(root_node):
                continue
            elif last_pos == jpos:
                if best_distance == -1 or len(root_node) - 1 < best_distance:
                    best_distance = len(root_node) - 1
            elif best_distance != -1 and len(root_node) - 1 >= best_distance:
                continue
            
            shortests_paths[last_pos] = len(root_node)
            #Add candidates from current node
            candidates = []
            candidates.append(tuple(map(operator.add, last_pos, (0, 1))))
            candidates.append(tuple(map(operator.add, last_pos, (0, -1))))
            candidates.append(tuple(map(operator.add, last_pos, (1, 0))))
            candidates.append(tuple(map(operator.add, last_pos, (-1, 0))))
            tmp = []
            for c in candidates:
                if maze[c[1]][c[0]] != '#' and not c in root_node:
                    queue.append(root_node + [c])

            #sort queue by distance
            queue = sorted(queue, key=distance)
        return best_distance
    
    distances = {}
    for i in positions.keys():
        for j in positions.keys():
            if i == j:
                continue
            ipos = positions[i]
            jpos = positions[j]
            distances.setdefault(i, {})
            distances.get(i)[j] = -1
            if distances.get(j, {}).get(i, -1) != -1:
                distances[i][j] = distances[j][i]
            else:
                distances[i][j] = calculate_distance(maze, ipos, jpos)
    
    p = [p for p in positions.keys() if p != '0']
    permutations = list(itertools.permutations(p))
    
    best_distance = -1
    for position_list in permutations:
        current_distance = 0
        current_position = '0'
        for pos in list(position_list) + ['0']:
            current_distance += distances[current_position][pos]
            current_position = pos
            if best_distance != -1 and current_distance > best_distance:
                break
        else:
            best_distance = current_distance
    print best_distance

            

if __name__ == '__main__':
    main()
