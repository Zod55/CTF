from pwn import *
import os


r,w = os.pipe()
s = ssh(host="pwnable.kr",port=2222,user="random",password="guest")

target = 3735928559
not_rand =1804289383
key = target ^ not_rand
os.write(w,key)
p = s.process("random",cwd="/home/random",stdin=r)
p.interactive()

