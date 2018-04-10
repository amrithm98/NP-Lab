from threading import Thread

def add(a,b,id):
    c = a+b
    print(str(id) + " "+ str(c))

t1 = Thread(add,(4,5,1))
t2 = Thread(add,(6,11,2))

t1.start()
t2.start()
t1.join()
t2.join()
