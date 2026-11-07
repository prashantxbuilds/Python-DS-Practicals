
queue = []

while True:
    print("\n1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check Queue Empty")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        cid = input("Enter Customer ID: ")
        time = int(input("Enter Call Time (minutes): "))
        queue.append([cid, time])
        print("Call Added")

    elif ch == 2:
        if len(queue) > 0:
            print("Answered Call:", queue.pop(0))
        else:
            print("Queue is Empty")

    elif ch == 3:
        print("Call Queue:", queue)

    elif ch == 4:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue is Not Empty")

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
