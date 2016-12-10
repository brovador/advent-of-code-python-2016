#encoding: utf-8
import re

def main():
    input_file = './input.txt'

    with open(input_file) as f:
        instructions = f.read().split('\n')
    
    commands = {
        'value' : re.compile(r'value (\d+) goes to bot (\d+)'),
        'gives' : re.compile(r'bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)'),
    }

    def command_value(m):
        value, botn = m.groups()
        value = int(value)
        bots.setdefault(botn, []).append(value)
        return True
    
    def command_gives(m):
        botn, o1, on1, o2, on2 = m.groups()
        chips = sorted(bots.get(botn, []))
        success = False

        if chips == [17, 61]:
            print 'Bot {0} has chips 61, 17'.format(botn)

        if len(chips) == 2:
            gives = ((o1, on1), (o2, on2))
            for i, chip in enumerate(chips):
                o, n = gives[i]
                if o == 'bot' and len(bots.get(n, [])) < 2:
                    bots.setdefault(n, []).append(chip)
                elif o == 'output':
                    outputs.setdefault(n, []).append(chip)
                else:
                    break
            else:
                success = True
        if success:
            bots[botn] = []
        return success
    
    bots = {}
    outputs = {}
    while (instructions):
        new_instructions = [x for x in instructions]
        for i in instructions:
            for command, pattern in commands.iteritems():
                m = pattern.match(i)
                if not m: continue

                success = False
                if command == 'value':
                    success = command_value(m)
                elif command == 'gives':
                    success = command_gives(m)
                
                if success:
                    new_instructions.remove(i)
        instructions = new_instructions
        


if __name__ == '__main__':
    main()