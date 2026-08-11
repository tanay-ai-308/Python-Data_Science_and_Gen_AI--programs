import sys

def main():
	
	if(len(sys.argv) == 3) :

		File = sys.argv[1]
		String = sys.argv[2]

		Ret = ChkString(File,String)
		print(f"string {String} is present {Ret} times in file {File}.")

	else :
		print("Please give input as :- ")
		print("\tpython fileName.py File.txt \"anystring\"")

def ChkString(File, Str) :

	fObj = open(File,'r')
	Count = 0

	Data = fObj.read()
	Words = Data.split()

	for word in Words :
		if (word == Str):
			Count += 1

	return Count
if __name__ == "__main__" :
	main()