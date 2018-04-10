from threading import Thread

class Semaphore(object):

    def __init__(self, initial_value):
        self.n = initial_value

    def wait(self):
        while(self.n <= 0):
   #         print ("----- Blocked ------")
	     pass
	self.n -= 1
    
    def signal(self):
        self.n += 1

class Reader_Writer(object):
    def __init__(self):
        self.rw_mutex = Semaphore(1)
        self.read_count = 0
        self.mutex = Semaphore(1)
        self.shared_memory = []

    def reader(self):
        self.mutex.wait()
        self.read_count += 1
        if (self.read_count == 1):
            self.rw_mutex.wait()
        self.mutex.signal()

        print ("Printing the contents of the list --> ", self.shared_memory)

        self.mutex.wait()
        self.read_count -= 1
        if (self.read_count == 0):
            self.rw_mutex.signal()
        self.mutex.signal()

    def writer(self):
        self.rw_mutex.wait()

        print ("Enter a string which is to be added to the shared memory:-")
        update = raw_input()
        self.shared_memory += [update]
	
        self.rw_mutex.signal()

        print ("Shared Memory Updated")
    
def test_thread(obj, t_id, num_operations = 10):
    for i in range(num_operations):
        if (i%10 == 0):
            print ("Thread : ", t_id, " executing Writer")
	    print 
            obj.writer()
        else:
            print ("Thread : ", t_id, " executing Reader")
            print
	    obj.reader()

if __name__ == "__main__":
    test_obj = Reader_Writer()
    thread1 = Thread(target = test_thread, args = (test_obj, 1, 10))
    thread2 = Thread(target = test_thread, args = (test_obj, 2, 10))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print ("\n -------------- EXIT --------------- \n")
