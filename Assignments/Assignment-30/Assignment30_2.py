import time
import datetime
import schedule

def main():
	
	schedule.every(1).minute.do(DisplayTime)

	while(1):
		schedule.run_pending()
		time.sleep(1)

def DisplayTime():
	print(datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

if __name__ == '__main__':
	main()


'''
NOTE :- 

datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

Yes, you want the time formatted exactly like:

Current Date and Time: 25-07-2026 04:30:00 PM

In Python, use the strftime() format:

%d-%m-%Y %I:%M:%S %p

Meaning:

%d → Day: 25
%m → Month: 07
%Y → Year: 2026
%I → Hour in 12-hour format: 04
%M → Minutes: 30
%S → Seconds: 00
%p → AM/PM: PM

'''