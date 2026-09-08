import os
import schedule
import time

def DirectoryScanner():

	DirectoryName = None;
	SubFolderCount = 0
	FileCount = 0

	for FolderName ,SubFolder ,FileName in os.walk("Marvellous") :
	    DirectoryName = os.path.abspath("Marvellous")
	    for Subf in SubFolder:
	       	SubFolderCount += 1
	    for fName in FileName :
	        FileCount += 1

	print(f"Name of Directory = {DirectoryName}")
	print(f"Number of Sub Folders = {SubFolderCount}")
	print(f"Number of Files = {FileCount}")
	print(f"Scan time = {time.strftime("%d-%m-%Y %I:%M:%S %p")}")


def main():
    Border = "-=-"*15

    print(Border)
    print("Marvellous Automation Script")
    print(Border)
    print("\n")

    DirectoryScanner()

    print("\n")
    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)
   
if __name__ == "__main__" :
    main()