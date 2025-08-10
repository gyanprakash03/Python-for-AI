n = int(input("Enter the number of rows : "))

def printPattern(n):
    if n < 1:
        return

    print("*" * n)
    printPattern(n-1)


printPattern(n)