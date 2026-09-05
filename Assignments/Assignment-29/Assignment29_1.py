def main():
    FileName = input("Give File name: ")

    try:
        ChkFile(FileName)
        print(f"File {FileName} present.")
    except FileNotFoundError:
        print("File is not present in current directory.")

def ChkFile(FileName):

    fObj = open(FileName, "r")

if __name__ == "__main__":
    main()