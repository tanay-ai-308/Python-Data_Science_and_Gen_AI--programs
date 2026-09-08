import schedule
import time

def main():
	
	Message = input("Enter message :- ")
	Interval = int(input("Enter interval in seconds :- "))
	
	if(Interval > 0):
		schedule.every(Interval).seconds.do(Display,Message)

		while(1):
			schedule.run_pending()
			time.sleep(1)
	else :
		print("Give interval of atleast 1 second.")
		
def Display(Message):
	print(Message)

if __name__ == '__main__':
	main()