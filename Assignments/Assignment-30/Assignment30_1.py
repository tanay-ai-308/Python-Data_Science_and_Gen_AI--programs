import schedule
import time

def main():
	
	schedule.every(2).seconds.do(Display)

	while(1):
		schedule.run_pending()
		time.sleep(1)

def Display():
	print("Jay Ganesh...")

if __name__ == '__main__':
	main()