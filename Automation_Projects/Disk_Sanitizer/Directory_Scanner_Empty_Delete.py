##########################################################
#
#   Importing required libraries
#
##########################################################

import os
import sys
import time
import schedule

##########################################################
#
#   Function name  :  DirectoryScanner
#   Input          :  Name of Directory
#   Description    :  Deletes all empty files periodically
#   Date           :  19/07/2026   
#   Author         :  Tanay Suresh Dherange
#
##########################################################

def DirectoryScanner(DirectoryPath):
    Border = "-="*30
    TimeStamp = time.ctime()
    Ret = False

    LogFileName = "Marvellous %s.log"%(TimeStamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    
    Ret = os.path.exists(DirectoryPath)
    
    if(Ret == False):
        print(f"Marvellous automation errer : There is no such directory with name {DirectoryPath}.")
        return
    
    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print(f"Marvellous Automation error : {DirectoryPath} is not a directory.")
        return
    
    print("Log file gets createdwith name :- ",LogFileName)

    fObj = open(LogFileName,'w')
    fObj.write(Border+"\n")
    fObj.write("Marvellous Automation Script\n")
    fObj.write(Border+"\n")
    fObj.write("\nFiles from the Directory are :- \n\n")

    TotalFiles = 0
    EmptyFiles = 0

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath) :
        
        for fName in FileName :
            
            fName = os.path.join(FolderName,fName)
            fObj.write("\t"+fName+" : "+str(+os.path.getsize(fName))+"\n")
            TotalFiles += 1

            if(os.path.getsize(fName) == 0):
                os.remove(fName)
                EmptyFiles +=1

    print("Log File is Created.")
    fObj.write("\n"+Border+"\n")
    fObj.write("Total Files Scan = "+str(TotalFiles)+"\n")
    fObj.write("Total Empty Files deleted = "+str(EmptyFiles)+"\n")
    fObj.write("\n"+Border+"\n")
    fObj.write("Logfile gets created at - "+str(TimeStamp)+"\n")
    fObj.write(Border+"\n")
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

##########################################################
#
#   Function name :  main
#   Input         :  Command line arguments
#   Description   :  It controls the script
#   Date          :  19/07/2026   
#   Author        :  Tanay Suresh Dherange
#
##########################################################

def main():

    HeaderBanner()
    
    if (len(sys.argv) == 2) :
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H") :
            print("\n-This Automation script is use to travel directory.")
            print("-For better usages please check --u flage.")
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U") :
            print("\n-Please execute script as :- ")
            print("\tpython Filename.py DirectoryName")
            print("-Directory name should be Absolute path")
        else :
            DirectoryName = sys.argv[1]
            #DirectoryScanner(DirectoryName)
            schedule.every(10).seconds.do(DirectoryScanner,DirectoryName)

            while(1):
                schedule.run_pending()
                time.sleep(1)
    else :
        print("Invalid Number of arguments.")
        print("Please use --h or --u for more information.")

    FooterBanner()


##########################################################
#
#   Starter of the automation script
#
##########################################################

if __name__ == "__main__" :
    main()