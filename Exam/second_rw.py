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
        self.r_count_mutex = Semaphore(1)
        self.w_count_mutex = Semaphore(1)
        self.mutex3 = Semaphore(1)
        self.read = Semaphore(1)
        self.write = Semaphore(1)
        self.shared_memory = []
        self.write_count = 0
        self.read_count = 0

    def reader(self):
        self.write = Semaphore(1)
        self.shared_memory = []
        self.write_count = 0
        self.read_count = 0

    def reader(self):
        self.mutex3.wait()
        self.read.wait()
        self.r_count_mutex.wait()

        self.read_count += 1
        if(self.read_count == 1):
            self.write.wait()

        self.r_count_mutex.signal()
        self.read.signal()
        self.mutex3.signal()

        print("\nPerforming Read Operation ",self.shared_memory)

        self.r_count_mutex.wait()

        self.read_count -= 1
        if(self.read_count == 0):
            self.write.signal()

        self.r_count_mutex.signal()


    def writer(self):

        self.w_count_mutex.wait()
        self.write_count += 1
        if(self.write_count == 1):
            self.read.wait()
        self.w_count_mutex.signal()

        #Perform Write
        self.write.wait()

        print("Enter Data: ")
        update = input()
        self.shared_memory += [update]
        
        self.write.signal()

        self.w_count_mutex.wait()
        self.write_count -= 1
        if(self.write_count == 0):
            self.read.signal()
        self.w_count_mutex.signal()


def test_thread(obj,id,num_ops = 10):
    for i in range(num_ops):
        if(i % 10 == 3):
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