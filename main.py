with open('input.txt', 'rt') as f:
    inp = f.read()

ONE   = ' '
ZERO  = '\t'
    
with open('output.txt', 'wt') as f:
    func = lambda x : ONE if x == '1' else ZERO
    for c in inp:
        c = bin(ord(c))[2:]
        l = ''.join(list(map(func, c)))
        f.write(l + '\n')

with open('output.txt', 'rt') as f:
    out = ''
    for c in f.read():
        if   c ==  ONE: out += '1'
        elif c == ZERO: out += '0'
        else : out += ' '
    for c in out.split(' '):
        if len(c) > 0:
            c = chr(int(c, 2))
            print(c, end='')
