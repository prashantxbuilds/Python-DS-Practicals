
queue = []

while True:
    print("\n1. Add Event")
    print("2. Process Event")
    print("3. Display Events")
    print("4. Cancel Event")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        event = input("Enter event: ")
        queue.append(event)
        print("Event Added")

    elif ch == 2:
        if len(queue) > 0:
            print("Processed Event:", queue.pop(0))
        else:
            print("Queue is Empty")

    elif ch == 3:
        print("Pending Events:", queue)

    elif ch == 4:
        event = input("Enter event to cancel: ")
        if event in queue:
            queue.remove(event)
            print("Event Cancelled")
        else:
            print("Event Not Found")

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
