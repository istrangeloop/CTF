from pwn import remote
import re
r = remote('195.154.53.62', 1337)
while True:
    robot = r.recvuntil(["=", "}"])
    expression = re.search(r"Question\s+\d+\s+:[\r\n\t\s]+([^=]+)", robot)
    print(robot)
    r.sendline(str(eval(expression.group(1))))

flag = r.recv(2048)
print(flag)
