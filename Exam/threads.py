from threading import Thread

def add(a,b,id):
    print("Sum from Thread %d is %d",id,a+b)

t1 = Thread(target=add,args=(5,4,1))
t2 = Thread(target=add,args=(1,2,2))

t1.start()
t2.start()

t1.join()
t2.join()
