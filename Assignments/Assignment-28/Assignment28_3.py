def main():
    FileName = input("Give File name: ")

    try:
        DisplayLine_Line(FileName)
    except FileNotFoundError:
        print("File is not present in the current directory.")

def DisplayLine_Line(FileName):

    print(f"Printing the {FileName} line by line :- ")
    
    fObj = open(FileName, "r")

    for line in fObj:
        print(line)

    fObj.close()

if __name__ == "__main__":
    main()