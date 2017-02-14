from pwn import process
from itertools import permutations

# 8lnucoitsrgnl8  19v9Zhik2y6TBpEZmFeCyEZRhEm1FFDLvV
bitcoin = '17iUnGoZbFrGS7uU9z2d2yRT9BKgVqnKnn'

fill = [''.join(p) for p in permutations('ucoitsgr')]

# vamo fazer um teste
for i in fill:
    trial = '8ln' + i + 'nl8'
    p = process(['python2','addressgen.py', trial], level='error')
    p.recvuntil('ress: ')
    stdout = p.recv(128).rstrip()
    print trial, bitcoin, stdout

    # evil happens here
    if bitcoin == stdout:
        print trial
        break
    p.kill()
