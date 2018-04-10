from threading import Thread

class Semaphore(object):
    def __init__(self,init_val):
        self.n = init_val

    def wait(self):
        while(self.n <= 0):
            pass
        self.n -=1
    
    def signal(self):
        self.n += 1

class ReaderWriter(object):
    def __init__(self):
        self.rw_mutex = Semaphore(1)
        self.mutex = Semaphore(1)
        self.shared_memory = []
        self.read_count = 0

    def reader(self):
        self.mutex.wait()
        self.read_count += 1
        if(self.read_count == 1):
            self.rw_mutex.wait()
        self.mutex.signal()

        print("\nPerforming Read Operation ",self.shared_memory)

        self.mutex.wait()
        self.read_count -= 1
        if(self.read_count == 0):
            self.rw_mutex.signal()
        self.mutex.signal()

    def writer(self):
        self.rw_mutex.wait()
        
        print("\nEnter Data : ")
        data = input()
        self.shared_memory += [data]

        print("\nMemory Updated as ",self.shared_memory)

        self.rw_mutex.signal()


def test_thread(obj,id,num_ops = 10):
    for i in range(num_ops):
        if(i % 10 == 0):
            print("\nThread "+str(id)+" Executing Writer ")
            obj.writer()
        else:
            print("\nThread "+str(id)+" Executing Reader ")
            obj.reader()

if __name__ == "__main__":
    obj = ReaderWriter()
    thread1 = Thread(target = test_thread,args = (obj,1))
    thread2 = Thread(target = test_thread,args = (obj,2))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("\nDone Simulation")