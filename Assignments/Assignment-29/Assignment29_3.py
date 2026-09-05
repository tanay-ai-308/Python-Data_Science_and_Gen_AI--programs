import sys

def main():

    if (len(sys.argv)<2 ):
        print("Please give file.")
        return
    elif(len(sys.argv)>2) :
        print("Only one file is required.")
        returns

    FileName = (sys.argv[1])

    try:
        CreateCopyFile(FileName)
        print("Copy created successfully.")
    except FileNotFoundError:
        print("File is not present in current directory.")

def CreateCopyFile(FileName):
    
    fObjOrg = open(FileName, "r")
    fObjCopy = open(FileName+" (Copy)", "w")

    Data = fObjOrg.read()
    fObjCopy.write(Data)

    fObjOrg.close()
    fObjCopy.close()

if __name__ == "__main__":
    main()