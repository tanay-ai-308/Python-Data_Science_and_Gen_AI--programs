import threading

def main() :

	Thread1 = threading.Thread(target = Print1_50)
	Thread2 = threading.Thread(target = Print50_1)

	Thread1.start()
	Thread1.join()

	Thread2.start()
	Thread2.join()

def Print1_50() :

	for i in range(1,51,1) :
		print(i)

def Print50_1() :

	for i in range(50,0,-1) :
		print(i)

if __name__ == '__main__':
	main()