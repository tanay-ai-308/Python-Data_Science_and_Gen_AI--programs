import time
import datetime
import schedule

def main():
	
	schedule.every().day.at("11:16").do(Display1)
	schedule.every().day.at("11:17").do(Display2)

	while(1):
		schedule.run_pending()
		time.sleep(1)

def Display1():
	print("Lunch Time..!🍽️🍜")

def Display2():
	print("Wrap up work..!😁")

if __name__ == '__main__':
	main()