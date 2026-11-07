
undo = []
redo = []
document = ""

while True:
    print("\n1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        undo.append(document)
        document += input("Enter text: ")
        redo = []

    elif ch == 2:
        if len(undo) > 0:
            redo.append(document)
            document = undo.pop()
        else:
            print("Nothing to Undo")

    elif ch == 3:
        if len(redo) > 0:
            undo.append(document)
            document = redo.pop()
        else:
            print("Nothing to Redo")

    elif ch == 4:
        print("Document:", document)

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
