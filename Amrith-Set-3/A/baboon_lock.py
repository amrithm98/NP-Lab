from threading import Thread

class Semaphore(object):
	def __init__(self,initVal):
		self.n = initVal

	def wait(self):
		while(self.n <= 0):
			pass
		self.n -= 1

	def signal(self):
		self.n += 1

class EastWest(object):

	def __init__(self):
		self.east = Semaphore(1)
		self.west = Semaphore(1)
		self.east_count = 0

	def eastWard(self):

		self.east.wait()
		self.east_count += 1
		if(self.east_count == 1):
			self.west.wait()
		self.east.signal()

		print("Baboon moving east")
		
		self.east.wait()
		self.east_count -= 1
		if(self.east_count == 0):
			self.west.signal()
		self.east.signal()

	def westWard(self):

		self.west.wait()

		print("Baboon Moving west & Current EAST COUNT IS " + str(self.east_count))

		self.west.signal()

def test_baboons(obj,id,ops):

	for i in range(ops):
		if(i % ops == 2):
			print("-----------------Baboon Coming WEST-----------------------------")
			obj.westWard()
		else:
			print("-----------------Baboon Coming EAST-----------------------------")
			obj.eastWard()
	print("Thread " + str(id) + " Complete")


if __name__ == "__main__":

	obj = EastWest()

	t1 = Thread(target=test_baboons,args = (obj,1,3))
	t2 = Thread(target=test_baboons,args = (obj,2,3))

	t1.start()
	t2.start()

	t1.join()
	t2.join()
