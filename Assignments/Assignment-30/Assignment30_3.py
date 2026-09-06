import time
import datetime
import schedule

def main():
	
	schedule.every(30).minutes.do(Display)

	while(1):
		schedule.run_pending()
		time.sleep(1)

def Display():
	print("Coding Kar..!")

if __name__ == '__main__':
	main()