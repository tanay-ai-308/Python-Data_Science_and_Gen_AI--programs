import sys
import hashlib

def main():

    if (len(sys.argv) == 3):
        File1 = (sys.argv[1])
        File2 = (sys.argv[2])

        if(CompareFiles(File1,File2)) :
            print("Success.")
        else :
            print("Failure.")
    else :
        print("Need atleast 2 files.")

'''
def CompareFiles(File1,File2):
    
    fObj1 = open(File1, "r")
    fObj2 = open(File2, "r")

    for line1 in fObj1:
        for line2 in fObj2:
        for char1,char2 in line1,line2:
            if (char1 != char2):
                return False

    return True        
'''

def CompareFiles (File1, File2) :

    fObj1 = open(File1,"rb")
    fObj2 = open(File2,"rb")

    hObj1 = hashlib.md5()
    hObj2 = hashlib.md5()

    Buffer1 = fObj1.read(1000)
    Buffer2 = fObj2.read(1000)

    while(Buffer1 and Buffer2) :
        
        hObj1.update(Buffer1)
        hObj2.update(Buffer2)
        
        Buffer1 = fObj1.read(1000)
        Buffer2 = fObj2.read(1000)

    if (Buffer1 or Buffer2) :
        return False

    fObj1.close()
    fObj2.close()

    return (hObj1.hexdigest() == hObj2.hexdigest())


if __name__ == "__main__":
    main()