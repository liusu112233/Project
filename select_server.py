"""

"""
from socket import *
from select import select

s = socket()
s.bind(("127.0.0.1", 2222))
s.listen(3)
s.setblocking(False)
rlist = [s]
wlist = []
xlist = []
while True:
    print("等待处理IO......")
    rs, ws, xs = select(rlist, wlist, xlist)
    print(rs)
    for r in rs:
        if r is s:
            c,addr =r.accept()
            print("Connect from",addr)
            c.setblocking(False)
            rlist.append(c)
        else:
            data =r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            r.send(b"OK")
            # rlist.append(r)
    for w in ws:
        # w.send(b"ok")
        # wlist.remove(w)
        pass

