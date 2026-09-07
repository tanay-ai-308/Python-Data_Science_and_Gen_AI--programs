import time
import datetime
import schedule

def main():
	
	schedule.every(1).minutes.do(Display)

	while(1):
		schedule.run_pending()
		time.sleep(1)

def Display():

	fObj = open("Marvellous.txt","a")

	fObj.write("Task Executed at :- "+datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")+"\n")

if __name__ == '__main__':
	main()