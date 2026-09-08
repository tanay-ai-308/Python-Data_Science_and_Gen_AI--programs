import os
import sys
import time
import schedule
#import datetime

def main():

    MonitorDirectory()

def MonitorDirectory() :

    if (sys.argv[1] == "--H" or sys.argv[1] == "--h") :
        print("-This Script is use to Monitor a given Directory.")
        print("-This script will Create a log file name DirectoryCountLog.txt.")
        print("-And Create a log of the file count in that log file after every 5 minutes.")
        print("-For how to use this script enter python Filename.py --u")
        return
    elif (sys.argv[1] == "--u" or sys.argv[1] == "--U") :
        print("-To Run this Script give the input as :- ")
        print("-   python FileName.py DirectoryName.")
        return
    elif(len(sys.argv) < 1):
        print("Get details about this script use --u or --h.")
        return

    DirectoryName = sys.argv[1]

    if (os.path.exists(DirectoryName) == False):
        print("Error: Directory does not exist.")
        return

    if (os.path.isdir(DirectoryName) == False):
        print("Error: The given path is not a directory.")
        return

    print(f"\nMonitoring directory: {DirectoryName}")
    print("File count will be recorded every 5 minutes.")

    schedule.every(1).minutes.do(CheckDirectory,DirectoryName)

    while True :
        schedule.run_pending()
        time.sleep(1)

def CheckDirectory (DirectoryName) :

    Log = CreateLog(DirectoryName)

    fObj = open("DirectoryCountLog.txt",'a')

    fObj.write(Log)

    fObj.close()

    print("Log entered.")

def CreateLog(DirectoryName) :

    FileCount = CountFiles(DirectoryName)

    DirectoryPath = os.path.abspath(DirectoryName)

    Date = time.strftime("%d-%m-%y")
    Time = time.strftime("%I:%M:%S %p")

    Log = "\n\n - Directory path = "+DirectoryPath+"\n - Number of Files = "+str(FileCount)+"\n - Date = "+Date+"\n - Time = "+Time+"\n\n"+("-=-"*30)+"\n"

    return Log

def CountFiles(DirectoryName) :

    FileCount = 0

    for FolderName ,SubFolderName ,FileName in os.walk(DirectoryName):
        for fName in FileName :
            FileCount += 1

    return FileCount

if __name__ == "__main__":
    main()