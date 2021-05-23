list_item=input("Enter Number Series:")
list_split=list_item.split(",")

#num = []
#for i in list_split:
#    num.append(int(i))

num= [int(i) for i in list_split]
print("Length of the list is:", len(num))
print(" ")

num.sort()
print("Sorted Numbers: ", end="")
for i in range (len(num)):
     print(num[i], end=" ")

print(" ")

search= int(input("Enter the Search Item:"))

first= 0
last= len(num)-1
mid= 0
gate=True

if search>=num[first] and search<=num[last]:
    print("Search Item in the list")
    while (first <= last) and gate:
        mid = (first + last) // 2
        if num[mid] == search:
            print("Search Item Found in Index:", mid)
            break

        elif num[mid] < search:
            first = mid + 1
        else:
            last = mid - 1

else:
    print("Search Item not Found")

