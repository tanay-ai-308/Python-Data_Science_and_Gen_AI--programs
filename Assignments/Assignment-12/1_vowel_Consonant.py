def main() :
	print("Enter a Character :- ")
	Letter = input()

	Ret = CheckVowel(Letter)

	if (Ret) :
		print(Letter,"is a vowel.")
	else :
		print(Letter,"is a consonent.")

def CheckVowel(Char) :
	
	if(Char == 'A' or Char =='E' or Char =='I' or Char =='O' or Char =='U' 
		or Char =='a' or Char =='e' or Char =='i' or Char =='o' or Char =='u') :
		return 1
	else :
		return 0

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter a Character :-
A
A is a vowel.

'''