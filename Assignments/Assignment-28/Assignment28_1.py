def main():
    FileName = input("Give File name: ")

    try:
        NoOfLines = CountLines(FileName)
        print(f"File {FileName} contains {NoOfLines} lines.")
    except FileNotFoundError:
        print("File is not present in current directory.")

def CountLines(FileName):
    count = 0

    fObj = open(FileName, "r")

    for line in fObj:
    	count += 1

    return count

if __name__ == "__main__":
    main()