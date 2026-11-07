
ids = [101, 105, 110, 115, 120, 125]
key = int(input("Enter Customer ID: "))

# Linear Search
found = 0
for i in range(len(ids)):
    if ids[i] == key:
        found = 1
        break

if found == 1:
    print("Linear Search: ID Found")
else:
    print("Linear Search: ID Not Found")

# Binary Search
low = 0
high = len(ids) - 1
found = 0

while low <= high:
    mid = (low + high) // 2

    if ids[mid] == key:
        found = 1
        break
    elif key < ids[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found == 1:
    print("Binary Search: ID Found")
else:
    print("Binary Search: ID Not Found")
