# printning triangle

n = int(input("Enter the number of rows : "))

maxStars = (2*n)-1

for i in range(1, n+1):
    stars = (2*i)-1
    spaces = (maxStars - stars)//2

    print(" " * spaces, end="")

    print("*" * stars, end="")

    print()