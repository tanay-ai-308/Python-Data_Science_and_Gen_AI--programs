'''
python DirectorySanitizer.py     2           FolderName       receiver@gmail.com        DemoFolder
pyton      filename       (time interval) (Directory name) (email to send log files) (LogFile Folder) 
              0                  1               2                    3                     4
'''
import os
import sys
import time
import hashlib
import schedule

from email.message import EmailMessage
import smtplib

from email.mime.base import MIMEBase
from email import encoders


def main():

    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("\nYou can run this script as :- ")
            print(f"\t1] {sys.argv[1]} 2 Foldername.")
            print(f"\t - File will get removed and logfile will get stored in folder DublicateFileRemovalLog.\n")
            print(f"\t2] {sys.argv[1]} 2 Foldername DemoFolder")
            print(f"\t - File will get removed and logfile will get stored in folder with given name.\n")
            print(f"\t3] {sys.argv[1]} 2 Foldername recivere@gmail.com")
            print(f"\t - File will get removed and logfile will be sent directly to the email.\n")
            print(f"\t4] {sys.argv[1]} 2 Foldername recivere@gmail.com DemoFolder")
            print(f"\t - File will get removed and logfile will get stored in folder name as well as the mail will be sent.\n")
            
        elif (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("\nThis Automation script is used to perform :-")
            print("\t1] To remove all the dublicate file from a given directory.")
            print("\t2] And creates the log file with details : ")
            print("\t\t - Starting time of Directory Scanning.")
            print("\t\t - Completion time of Directory Scanning.")
            print("\t\t - Name of the Directory Scanned.")
            print("\t\t - Total number of file Scanned.")
            print("\t\t - Total number of dublicate files found.")
            print("\t\t - Total number of dublicate files deleted.")
            print("\t\t - Complete path of all deleted dublicate files.")
            print("\t\t - Errors encountered during execution.")
            print("\t\t - Email delivery status.")
            print("\t3] This script will run every after every interval of time given by you.")
            print("\t4] And this log file will be send to the email if given.")
            print("\t5] Or the Folder will get created in the current directory named as given or by DublicateFileRemovalLog.")
            print("\t6] It Maintains all records in log Folder.")
            print("\t7] It sends the log file through mail periodically as per time Interval.")
            print("\nUse --u to know how to use this script.")

        else :
            print(" - Use --h or --u to get more information about script.")
   
    elif(len(sys.argv) == 3):
        ScheduleWork(int(sys.argv[1]),sys.argv[2])
    elif(len(sys.argv) == 4):
        ScheduleWork(int(sys.argv[1]),sys.argv[2],sys.argv[3])
    elif(len(sys.argv) == 5):
        ScheduleWork(int(sys.argv[1]),sys.argv[2],sys.argv[3],sys.argv[4])
    else :
        print("Use --h or --u to get information about script.")

def ScheduleWork(Time,DirectoryName,Parameter1 = False,Parameter2 = False):

    schedule.every(Time).seconds.do(DeleteDuplicate,DirectoryName,Parameter1,Parameter2)

    while True :
        schedule.run_pending()
        time.sleep(1)


def CalculateChkSum(FileName) :
    
    fObj = open(FileName,'rb')
    hObj = hashlib.md5()

    Buffer = fObj.read(1024)

    while(len(Buffer)) :
        hObj.update(Buffer)
        Buffer = fObj.read(1024)

    fObj.close()

    return hObj.hexdigest()

def FindDuplicate(DirectoryName) :

    Ret = False
    Duplicate = dict()

    Ret = os.path.exists(DirectoryName)

    if (Ret == False) :
        print("Path is invalid")
        exit()

    Ret = os.path.isdir(DirectoryName)

    if (Ret == False) :
        print("It is not a Directory.")
        exit()

    for FolderName ,SubFolderName ,FileName in os.walk(DirectoryName) :

        for fName in FileName :
            fName = os.path.join(FolderName,fName)

            ChkSum = CalculateChkSum(fName)

            if (ChkSum in Duplicate) :
                Duplicate[ChkSum].append(fName)
            else :
                Duplicate[ChkSum] = [fName]

    return Duplicate

def DeleteDuplicate(DirectoryName,Parameter1 = False,Parameter2 = False):

    Path = list()
    TimeStamp = time.ctime()
    
    LogFileName = "Marvellous %s.log"%(TimeStamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    StartTime = time.ctime()

    Email = False
    Directory = False

    Count = 0
    TotalDeleted = 0

    if (Parameter1 != False) :
        if '@' in Parameter1 :
            Email = Parameter1
            if (Parameter2 != False) :
                Directory = Parameter2
        else :
            Directory = Parameter1
            if (Parameter2 != False) :
                Email = Parameter2

    
    MyDict = FindDuplicate(DirectoryName)
    
    Result = list(filter(lambda X : len(X)>1,MyDict.values()))

    TotalDublicateFiles = 0
    for Value in Result :
        for SubValue in Value :
            Count += 1
            if (Count > 1):
                TotalDublicateFiles = TotalDublicateFiles+ 1
                try:
                    os.remove(SubValue)
                    Path.append(SubValue)
                    TotalDeleted = TotalDeleted + 1

                except OSError as e:
                    print("Unable to delete:", SubValue)

        Count = 0

    EndTime = time.ctime()

    Log = CreateLog(MyDict,TotalDeleted,TotalDublicateFiles,StartTime,EndTime,Path)
    
    if Email :
        SendMail(LogFileName,Log,Email)

    if Directory :
        CreateLogFile(LogFileName,Log,Directory)

def CreateLogFile(LogFileName,Log,FolderName=False):

    Border = "-="*30

    if FolderName:
        os.makedirs(FolderName, exist_ok=True)
        LogFileName = os.path.join(FolderName, LogFileName)

    fObj = open(LogFileName,'w')
    fObj.write(Border+"\n")
    fObj.write("Marvellous Automation Script\n")
    fObj.write(Border+"\n")
    fObj.write("\nAutomation Script Updates :- \n")
    fObj.write(Log+"\n")
    fObj.write("\n"+Border+"\n")
    fObj.close()

    return LogFileName

def SendMail(LogFileName,Log,Reciver):

#=======================================================================
#       Assign your EMail Details To The Variable as
#
#   Sender = "YourEmail@gmail.com"
#   AppPassword = "tana yaya natu dyuq"  
#   Remove None And your Credentials
#=======================================================================
    Sender = None        # <== VARIABLE
    AppPassword = None   # <== AppPassword

    Message = EmailMessage()
    Message["From"] = Sender
    Message["To"] = Reciver

    
    Message["Subject"] = "Directory Sanitizer - Duplicate File Removal Report"

    Message.set_content(f"""
    
    Hello,

    Please find attached the Directory Sanitizer execution report.

    The report contains details about:
    - Directory scanned
    - Total files scanned
    - Duplicate files found
    - Duplicate files deleted
    - Paths of deleted files
    - Execution start and completion time
    - Errors encountered during execution

    Please refer to the attached log file for complete details.

    Regards,  
    {Sender}
    """)

    Attachment = MIMEBase("application", "octet-stream")

    LogFile = CreateLogFile(LogFileName,Log)
    
    with open(LogFile, "rb") as fObj:
        Attachment.set_payload(fObj.read())

    encoders.encode_base64(Attachment)

    Attachment.add_header(
        "Content-Disposition",
        f"attachment; filename={os.path.basename(LogFile)}"
    )

    Message.attach(Attachment)
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(Message["From"], password = AppPassword)
    server.send_message(Message)
    server.quit()

    os.remove(LogFile)

def CreateLog(MyDict,TotalDeleted,TotalDublicateFiles,StartTime,EndTime,Path):

    TotalFiles = 0
    Border = "- - "*20

    for Values in MyDict.values():
        TotalFiles += len(Values)

    Log = "\n - Starting time of Directory Scanning     = "+str(StartTime)+"\n"
    Log = Log+Border+"\n"
    Log = Log+"\n - Completion time of Directory Scanning   = "+str(EndTime)+"\n"
    Log = Log+Border+"\n"
    Log = Log+"\n - Name of the Directory Scanned           = "+sys.argv[2]+"\n"
    Log = Log+Border+"\n"
    Log = Log+"\n - Total number of file Scanned            = "+str(TotalFiles)+"\n"
    Log = Log+Border+"\n"
    Log = Log+"\n - Total number of dublicate files found   = "+str(TotalDublicateFiles)+"\n"
    Log = Log+Border+"\n"
    Log = Log+"\n - Total number of dublicate files deleted = "+str(TotalDeleted)+"\n"
    Log = Log+Border+"\n"
    Log = Log+"\n - Complete path of all deleted dublicate files."+"\n"
    for i in range (0,len(Path)):
        Log = Log+"\n\t -=> "+str(Path[i]) 
    Log = Log+"\n"+Border+"\n"

    return Log


if __name__ == "__main__" :
    main()