row= int(input("Enter row:"))

i= 1

while i <= row:
    j= 0
    while j < i:
        print("*", end="")
        j= j+1
    print("")
    i = i + 1