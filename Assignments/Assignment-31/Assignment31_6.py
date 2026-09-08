import schedule
import time

def main():
	
	schedule.every().monday.at("9:30").do(Display,"Start your weekly goals.")
	schedule.every().wednesday.at("17:00").do(Display,"Review your weekly progress.")
	schedule.every().friday.at("18:00").do(Display,"Weekly work completed.")

	while(1):
		schedule.run_pending()
		time.sleep(1)
	
def Display(Message):
	print(Message)

if __name__ == '__main__':
	main()