"""
第二是是是种方案
"""
from socket import *
from select import *

s = socket()
s.bind(("127.0.0.1", 2225))
s.listen(3)
s.setblocking(False)
p = epoll()
p.register(s, EPOLLIN)
fdmap = {s.fileno(): s}
while True:
    print("等待IO发生")
    events = p.poll()
    for fileno, event in events:
        if fileno is s.fileno():
            c, addr = fdmap[fileno].accept()
            print("Connect from", addr)
            c.setblocking(False)
            p.register(c, EPOLLIN|EPOLLET)
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:
            data = fdmap[fileno].recv(1024)
            if not data:
                p.unregister(fileno)
                fdmap[fileno].close()
                del fdmap[fileno]
                continue
            print(data.decode())
            fdmap[fileno].send(b"OK")
