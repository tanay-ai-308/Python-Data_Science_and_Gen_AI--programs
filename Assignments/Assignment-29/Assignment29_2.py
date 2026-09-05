def main():
    FileName = input("Give File name: ")

    try:
        DisplayFile(FileName)
    except FileNotFoundError:
        print("File is not present in the current directory.")

def DisplayFile(FileName):

    print(f"Printing the {FileName} line by line :- ")
    
    fObj = open(FileName, "r")

    Data = fObj.read()
    print("File Data :- \n")
    print(Data)
    
    fObj.close()

if __name__ == "__main__":
    main()