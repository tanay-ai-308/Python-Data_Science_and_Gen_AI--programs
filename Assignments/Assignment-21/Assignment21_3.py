import threading

def main():
	
	Count = [100]
	Lock = threading.Lock()

	print(Count)
	
	Tobj1 = threading.Thread(target=Function,args=(Count,Lock))
	Tobj2 = threading.Thread(target=Function,args=(Count,Lock))

	Tobj1.start()
	Tobj2.start()

	Tobj1.join()
	Tobj2.join()

def Function(Count,Lock):

	Lock.acquire()
	Count[0] = Count[0]+100
	Lock.release()

	print(Count)

if __name__ == '__main__':
	main()