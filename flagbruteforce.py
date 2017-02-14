from pwn import process
from time import sleep

trylist='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_'
i = 0
payload = 'ALEXCTF{'
while True:
    for k in trylist:
        sleep(0.01)
        nex = k
        flagtry = payload + nex
        re2 = process(['./re2', flagtry])
        hint =re2.recvall()
        i+=1
        if 'You should' in hint:
            payload = flagtry
            nex = 'A'
            break;
        print flagtry
