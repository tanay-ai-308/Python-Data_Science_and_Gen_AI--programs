def main() :

	ChkNum()

def ChkNum() :

	No = 1
	Count = 0
	while (Count<10):
		if(No%2 == 0):
			Count+=1
			print(No,end="	")
		No+=1

if __name__ == "__main__" :
	main()