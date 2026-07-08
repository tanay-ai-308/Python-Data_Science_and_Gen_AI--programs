import threading

def main() :

	print("Enter a string :- ")
	String = input()

	Tobj1 = threading.Thread(target = CountLowerCase,args=(String,),name = "CountLowerCase")
	Tobj2 = threading.Thread(target = CountUpperCase,args=(String,),name = "CountUpperCase")
	Tobj3 = threading.Thread(target = CountDigits,args=(String,),name = "CountDigits")

	Tobj1.start()
	Tobj2.start()
	Tobj3.start()

	Tobj1.join()
	Tobj2.join()
	Tobj3.join()

def CountLowerCase(String) :

	Count = 0

	for Char in String :
		if(Char>='a' and Char<='z') :
			Count += 1
	
	print(f"Total Small letters = {Count}")
	print(f"thread name = {threading.current_thread().name}")
	print(f"thread id of CountLowerCase = {threading.get_ident()}")

def CountUpperCase(String) :

	Count = 0

	for Char in String :
		if(Char>='A' and Char<='Z') :
			Count += 1

	print(f"Total Capital letters = {Count}")
	print(f"thread name = {threading.current_thread().name}")
	print(f"thread id CountUpperCase = {threading.get_ident()}")

def CountDigits(String) :

	Count = 0

	for Char in String :
		if(Char>='0' and Char<='9') :
			Count += 1

	print(f"Total Digits = {Count}")
	print(f"thread name = {threading.current_thread().name}")
	print(f"thread id CountDigits = {threading.get_ident()}")

if __name__ == '__main__':
	main()