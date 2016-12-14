#encoding: utf-8
import re
import itertools
import copy
import random

#magic: after several tries, this appears to be a good limit
best_solution = 40

def main():
    input_file = './input.txt'

    with open(input_file) as f:
        instructions = f.read().split('\n')
    
    pattern = re.compile(r'(\w+ generator|\w+-compatible microchip)')
    elements = []
    floors = []
    floors_history = {}

    for i in instructions:
        floor = {'G' : [], 'M' : []}
        for e in pattern.findall(i):
            element = e.replace('-compatible microchip', '').replace(' generator', '')
            if not element in elements: elements.append(element)
            if 'generator' in e:
                floor['G'].append(element)
            else:
                floor['M'].append(element)
        floors.append(floor)
    
    def print_floors(floors, elevator):
        s = []
        for i, f in enumerate(floors):
            fs = 'F{0} {1} '.format(i + 1, 'E' if elevator == i else '.')
            for e in elements:
                fs += ' ' + e[0].upper() + 'G' if e in floors[i]['G'] else ' . '
                fs += ' ' + e[0].upper() + 'M' if e in floors[i]['M'] else ' . '
            s.append(fs)
        print '*' * 20
        print '\n'.join(reversed(s)) 
        print '*' * 20
    
    def is_valid_setup(floors):
        for f in floors:
            if not (len(f['G']) == 0 or all([e in f['G'] for e in f['M']])):
                return False
            if f == floors[-1] and len(f['M']) >= 1 and len(f['G']) == 0:
                return False
        return True

    def perform_moves(floor_from, floor_to, moves):
        for m in moves:
            element_type, element = m.split('-') 
            floor_to[element_type].append(element)
            floor_from[element_type].remove(element)
    
    def perform_move(steps, floors, elevator_from, elevator_to, move):
        global best_solution
        elevator = elevator_to

        if all([len(floors[-1][x]) == len(elements) for x in 'GM']):
            if steps < best_solution:
                print 'Best solution found: ', steps 
                best_solution = steps
            return
        
        floor_candidates = []
        if elevator == 0:
            floor_candidates = [elevator + 1]
        elif elevator == len(floors) - 1:
            floor_candidates = [elevator - 1]
        else:
            floor_candidates = [elevator + 1, elevator - 1]
        
        valid_moves = []
        for floor_candidate in floor_candidates:
            current_floor = floors[elevator]

            candidates = []
            g = ['G-' + x for x in floors[elevator]['G']]
            m = ['M-' + x for x in floors[elevator]['M']]
            if floor_candidate > elevator:
                #going up
                candidates = list(itertools.combinations(g + m, 2)) + g + m
            else:
                #going down
                #only move down generators if not are in latest floor
                #candidates = m if elevator == len(floors) - 1 else g + m
                candidates = m + list(itertools.combinations(g + m, 2)) + g
            candidates = [list(c) if isinstance(c, tuple) else [c] for c in candidates] 
            
            
            duplicated_gm = []
            duplicated_m = []
            duplicaged_g = []
            duplicated_mm = []
            for candidate in candidates:
                if len(candidate) == 1:
                    element_type, element = candidate[0].split('-')
                    #we can clean duplicated when we move microchips associated to a generator individually
                    if element_type == 'M' and element in floors[elevator]['G']:
                        duplicated_m.append(candidate)
                    #we can clean when moving a generator associated to a microchip
                    if element_type == 'G' and element in floors[elevator]['M']:
                        duplicaged_g.append(candidate)
                elif len(candidate) == 2:
                    element_type1, element1 = candidate[0].split('-')
                    element_type2, element2 = candidate[1].split('-')
                    #we can clean all the duplicated moves (when moving generator and microchip)
                    #at the same time
                    if element1 == element2:
                        duplicated_gm.append(candidate)
                    #we can clean duplicated when we move microchips associated to a generator together
                    if element_type1 == element_type2 == 'M' and all([(x in floors[elevator]['G']) for x in [element1, element2]]):
                        duplicated_mm.append(candidate)
            items_to_remove = duplicated_gm[1:] + duplicated_m[1:] + duplicaged_g[1:] + duplicated_mm[1:] 
            for item in items_to_remove:
                candidates.remove(item)

            for candidate in candidates:
                if candidate == move and floor_candidate == elevator_from:
                    continue
                
                new_floors = [{'G' : f['G'][:], 'M' : f['M'][:]} for f in floors]
                new_floor = new_floors[floor_candidate]
                old_floor = new_floors[elevator]
                
                for m in candidate:
                    element_type, element = m.split('-')
                    new_floor[element_type].append(element)
                    old_floor[element_type].remove(element)

                history_value = str((floor_candidate, new_floors, ))
                if floors_history.get(history_value, steps) < steps:
                    continue
                floors_history[history_value] = steps
                
                if is_valid_setup(new_floors):
                    valid_moves.append((new_floors, floor_candidate, candidate))
        
        min_more_steps = sum([len(f['G']) + len(f['M']) * (len(floors) - i - 1) for i, f in enumerate(floors[:-1])])

        for move in valid_moves:
            if steps + min_more_steps >= best_solution:
                break
            perform_move(steps + 1, move[0], elevator, move[1], move[2])
    
    elevator = 0
    perform_move(0, floors, 0, 0, [])
    print best_solution


if __name__ == '__main__':
    main()