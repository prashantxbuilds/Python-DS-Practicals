
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


def minimum(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        temp = minimum(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


def display(root):
    if root is not None:
        display(root.left)
        print(root.data, end=" ")
        display(root.right)


root = None

while True:
    print("\n\n--- Binary Search Tree ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        data = int(input("Enter Value: "))
        root = insert(root, data)
        print("Value Inserted!")

    elif ch == 2:
        data = int(input("Enter Value to Delete: "))
        root = delete(root, data)
        print("Delete Operation Completed!")

    elif ch == 3:
        data = int(input("Enter Value to Search: "))

        if search(root, data):
            print("Element Found!")
        else:
            print("Element Not Found!")

    elif ch == 4:
        print("BST Elements (Ascending Order):")
        display(root)

    elif ch == 5:
        break

    else:
        print("Invalid Choice!")
