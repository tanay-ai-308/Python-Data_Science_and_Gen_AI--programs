def main():
    FileName = input("Give File name: ")

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