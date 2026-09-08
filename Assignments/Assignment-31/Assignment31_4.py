import time
import schedule

def CreateLog():

    TimeStamp = time.ctime()

    LogFileName = "Marvellous %s.log"%(TimeStamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    
    print("Log file gets createdwith name :- ",LogFileName)

    fObj = open(LogFileName,'w')
    
    fObj.write("Log file created successfully.\n")
    fObj.write("Creation time :- "+time.strftime("%d-%m-%Y %I:%M:%S %p"))
    
    fObj.close()

def HeaderBanner():
    Border = "-="*30

    print(Border)
    print("Marvellous Automation Script")
    print(Border)
    print("\n")

def FooterBanner():
    Border = "-="*30
    print("\n")
    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)
    print("\n")

def main():

    HeaderBanner()
    
    schedule.every(10).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(9)
    
    FooterBanner()
   
if __name__ == "__main__" :
    main()