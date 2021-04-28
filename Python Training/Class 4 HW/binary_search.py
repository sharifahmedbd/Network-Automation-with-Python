list_item=input("Enter Number Series:")
list_split=list_item.split(",")

#num = []
#for i in list_split:
#    num.append(int(i))

num= [int(i) for i in list_split]
print("Length of the list is:", len(num))
print(" ")

search= int(input("Enter the Search Item:"))

first= 0
last= len(num)-1
mid= 0

while (first<=last):
    mid=(first+last)//2
    if num[mid] == search:
        print("Search Found in Index:", mid)
        break

    elif num[mid]<search:
        first=mid + 1
    else:
        last = mid - 1

    if mid == -1:
        print("Search Item not Found")

