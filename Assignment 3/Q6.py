from sys import getsizeof

print("Enter data :- ")
val = input()

print("Type of val = ",type(val))			#type of val will always be str.
print("Memory address of val = ",id(val))
print("Size of val = ",getsizeof(val))

'''
note :- return type of input() is str by default.
		We can type caste it like this :
		int(input()),float(input()),set(input())... etc.
'''