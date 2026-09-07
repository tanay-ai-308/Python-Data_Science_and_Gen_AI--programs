import os
import sys
import time
import shutil
import schedule

def main():

	if (len(sys.argv) <= 3):
		if(len(sys.argv) < 3):
			if (sys.argv[1] == "--h" or sys.argv[1] == "--H") :
				print("\n-This Automation script is use to get backup of a given file after every 1 hour")
				print("-For better usages please check --u flage.")
			elif (sys.argv[1] == "--u" or sys.argv[1] == "--U") :
				print("\n-Please execute script as :- ")
				print("\tpython Filename.py Sourcefile.txt DirectoryName")
				print("-Directory name should be Absolute path")
			else :
				print("Use --h or --u to get more info about this script")

		else :
			SourceFile = sys.argv[1]
			DestinationPath = sys.argv[2]

			schedule.every(1).hour.do(Backup,SourceFile,DestinationPath)

			while(1):
				schedule.run_pending()
				time.sleep(1)


def Backup(SourceFile,DestinationPath):
    TimeStamp = time.strftime("%d-%m-%Y %I:%M:%S %p")
    Ret = False

    LogFileName = "%s.log"%(TimeStamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace("-","_")
    LogFileName = LogFileName.replace(":","_")

    Ret = os.path.exists(DestinationPath)
    
    if(Ret == False):
        print(f"Marvellous automation errer : There is no such directory with name {DestinationPath}.")
        return
    
    Ret = os.path.isdir(DestinationPath)

    if(Ret == False):
        print(f"Marvellous Automation error : {DestinationPath} is not a directory.")
        
        return
    
    print(f"Backup completed successfully at {TimeStamp}.\nLog file gets created with name :- {LogFileName}")

    fObj1 = open(LogFileName,'w')
    fObj2 = open(SourceFile,'r')
    
    Data2 = fObj2.read()
    
    fObj1.write(Data2)
    
    fObj2.close()
    fObj1.close()
    
    shutil.copy(LogFileName,DestinationPath)
    
    os.remove(LogFileName)

if __name__ == '__main__':
	main()