def main():
    FileName = input("Give File name - ")
    Keyword = input("Enter word to search - ")

    try:
        if(CountWords(FileName,Keyword)) :
            print(f"{Keyword} is present in file {FileName}.")
        else :
            print(f"{Keyword} is not present in file{FileName}.")
    except FileNotFoundError:
        print("File is not present in the current directory.")

def CountWords(FileName,Key):
    
    fObj =  open(FileName, "r")

    for line in fObj:
        for Word in line.split():
            if (Key == Word) :
                return True

    return False

if __name__ == "__main__":
    main()