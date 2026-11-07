
size = 10
hash_table = [None] * size

# Insert Key
def insert(key):
    index = key % size

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is None or hash_table[pos] == "DELETED":
            hash_table[pos] = key
            print("Key Inserted Successfully!")
            return

        if hash_table[pos] == key:
            print("Key Already Exists!")
            return

    print("Hash Table is Full!")


# Search Key
def search(key):
    index = key % size

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is None:
            break

        if hash_table[pos] == key:
            print("Key Found at Index:", pos)
            return

    print("Key Not Found!")


# Delete Key
def delete(key):
    index = key % size

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is None:
            break

        if hash_table[pos] == key:
            hash_table[pos] = "DELETED"
            print("Key Deleted Successfully!")
            return

    print("Key Not Found!")


# Display Hash Table
def display():
    print("\nHash Table:")

    for i in range(size):
        print(i, ":", hash_table[i])


# Main Menu
while True:
    print("\n--- Hash Table Operations ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        key = int(input("Enter Key: "))
        insert(key)

    elif ch == 2:
        key = int(input("Enter Key to Search: "))
        search(key)

    elif ch == 3:
        key = int(input("Enter Key to Delete: "))
        delete(key)

    elif ch == 4:
        display()

    elif ch == 5:
        break

    else:
        print("Invalid Choice!")
