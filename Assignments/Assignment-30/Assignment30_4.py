import time
import datetime
import schedule

def main():
	
	schedule.every().day.at("11:00").do(Display)

	while(1):
		schedule.run_pending()
		time.sleep(1)

def Display():
	print("Namaskar...")
	print(datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

if __name__ == '__main__':
	main()