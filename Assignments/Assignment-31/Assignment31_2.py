import schedule
import time

def main():
	
	Message = input("Enter message :- ")
	
	schedule.every(5).seconds.do(Display,Message)

	while(1):
		schedule.run_pending()
		time.sleep(1)
	
def Display(Message):
	print(Message)

if __name__ == '__main__':
	main()