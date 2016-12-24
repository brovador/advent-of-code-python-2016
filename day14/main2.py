#encoding: utf-8
import md5

def main():
    input_file = './input2.txt'

    with open(input_file) as f:
        salt = f.read()
    hashes = {}

    def generate_hash(i):
        if not i in hashes:
            m = md5.new()
            m.update(salt + str(i))
            s = m.hexdigest()
            for x in range(2016):
                m = md5.new()
                m.update(s)
                s = m.hexdigest()
            hashes[i] = s
        return hashes[i]
    
    def find_key(salt, i):
        found = False
        s = generate_hash(i)
        triple = None
        for j in range(0, len(s) - 2):
            triple = s[j] if s[j:j + 3] == s[j] * 3 else None
            if triple != None: break
        
        if triple:
            has_five = False
            for j in range(i + 1, i + 1000):
                s = generate_hash(j)
                for k in range(0, len(s) - 5):
                    has_five = s[k:k + 5] == triple * 5
                    if has_five: break
                found = has_five
                if found: break
        return found
    
    i = -1
    keys_found = 0
    while keys_found < 64:
        i += 1
        print i, keys_found
        if find_key(salt, i):
            keys_found += 1 
    print i

            



            


if __name__ == '__main__':
    main()