from pwn import *

r = remote("pwnable.kr",9025)
sleep(2)
r.recv()
r.sendline()
r.recv()
x = r.recv()

print(f"this is x {x}")
r.interactive()
