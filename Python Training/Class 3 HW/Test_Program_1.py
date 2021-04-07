row= int(input("Enter Row:"))
column= int(input("Enter Column:"))

i= 0

while i < row:
    j= 0
    while j<column:
        print("*", " ",  end="")
        j= j+1

    print("")
    i = i + 1

