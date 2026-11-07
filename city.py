
class Node:
    def __init__(self, city, population):
        self.city = city
        self.population = population
        self.left = None
        self.right = None


def insert(root, city, population):
    if root is None:
        return Node(city, population)

    if city < root.city:
        root.left = insert(root.left, city, population)
    elif city > root.city:
        root.right = insert(root.right, city, population)
    else:
        print("City Already Exists!")

    return root


def search(root, city):
    count = 0

    while root is not None:
        count += 1

        if city == root.city:
            print("City Found!")
            print("Population:", root.population)
            print("Comparisons:", count)
            return

        elif city < root.city:
            root = root.left
        else:
            root = root.right

    print("City Not Found!")
    print("Comparisons:", count)


def update(root, city, population):
    while root is not None:
        if city == root.city:
            root.population = population
            print("Population Updated!")
            return

        elif city < root.city:
            root = root.left
        else:
            root = root.right

    print("City Not Found!")


def minimum(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, city):
    if root is None:
        return None

    if city < root.city:
        root.left = delete(root.left, city)

    elif city > root.city:
        root.right = delete(root.right, city)

    else:
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        temp = minimum(root.right)
        root.city = temp.city
        root.population = temp.population
        root.right = delete(root.right, temp.city)

    return root


def ascending(root):
    if root:
        ascending(root.left)
        print(root.city, "-", root.population)
        ascending(root.right)


def descending(root):
    if root:
        descending(root.right)
        print(root.city, "-", root.population)
        descending(root.left)


root = None

while True:
    print("\n--- City Management Using BST ---")
    print("1. Add City")
    print("2. Delete City")
    print("3. Update Population")
    print("4. Search City")
    print("5. Ascending Order")
    print("6. Descending Order")
    print("7. Maximum Comparisons")
    print("8. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        city = input("Enter City Name: ")
        population = int(input("Enter Population: "))
        root = insert(root, city, population)

    elif ch == 2:
        city = input("Enter City to Delete: ")
        root = delete(root, city)
        print("Delete Operation Completed!")

    elif ch == 3:
        city = input("Enter City Name: ")
        population = int(input("Enter New Population: "))
        update(root, city, population)

    elif ch == 4:
        city = input("Enter City to Search: ")
        search(root, city)

    elif ch == 5:
        print("\nCities in Ascending Order:")
        ascending(root)

    elif ch == 6:
        print("\nCities in Descending Order:")
        descending(root)

    elif ch == 7:
        temp = [root]
        max_comparisons = 0

        while temp:
            node = temp.pop()
            if node:
                max_comparisons += 1
                temp.append(node.left)
                temp.append(node.right)

        print("Maximum Comparisons Required:", max_comparisons)

    elif ch == 8:
        break

    else:
        print("Invalid Choice!")
