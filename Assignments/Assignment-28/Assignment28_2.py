def main():
    FileName = input("Give File name: ")

    try:
        NoOfWords = CountWords(FileName)
        print(f"File '{FileName}' contains {NoOfWords} words.")
    except FileNotFoundError:
        print("File is not present in the current directory.")

def CountWords(FileName):
    count = 0

    with open(FileName, "r") as fObj:
        for line in fObj:
            words = line.split()
            count += len(words)

    return count

if __name__ == "__main__":
    main()