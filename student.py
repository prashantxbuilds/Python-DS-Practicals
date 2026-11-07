
class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

head = None

while True:
    print("\n1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Sort Records")
    print("6. Display Records")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        new = Node(roll, name, marks)

        if head == None:
            head = new
        else:
            temp = head
            while temp.next != None:
                temp = temp.next
            temp.next = new

        print("Student Added")

    elif ch == 2:
        roll = int(input("Enter Roll No to Delete: "))
        temp = head
        prev = None

        while temp != None and temp.roll != roll:
            prev = temp
            temp = temp.next

        if temp == None:
            print("Student Not Found")
        elif prev == None:
            head = temp.next
            print("Student Deleted")
        else:
            prev.next = temp.next
            print("Student Deleted")

    elif ch == 3:
        roll = int(input("Enter Roll No to Update: "))
        temp = head

        while temp != None and temp.roll != roll:
            temp = temp.next

        if temp == None:
            print("Student Not Found")
        else:
            temp.name = input("Enter New Name: ")
            temp.marks = float(input("Enter New Marks: "))
            print("Student Updated")

    elif ch == 4:
        roll = int(input("Enter Roll No to Search: "))
        temp = head

        while temp != None and temp.roll != roll:
            temp = temp.next

        if temp == None:
            print("Student Not Found")
        else:
            print(temp.roll, temp.name, temp.marks)

    elif ch == 5:
        order = input("Sort by (1.Roll No / 2.Marks): ")
        direction = input("Ascending or Descending (A/D): ")

        temp = head
        while temp != None:
            p = temp.next
            while p != None:
                if order == "1":
                    swap = temp.roll > p.roll if direction == "A" else temp.roll < p.roll
                else:
                    swap = temp.marks > p.marks if direction == "A" else temp.marks < p.marks

                if swap:
                    temp.roll, p.roll = p.roll, temp.roll
                    temp.name, p.name = p.name, temp.name
                    temp.marks, p.marks = p.marks, temp.marks

                p = p.next
            temp = temp.next

        print("Records Sorted")

    elif ch == 6:
        temp = head

        if temp == None:
            print("No Records Found")
        else:
            print("Roll No\tName\tMarks")
            while temp != None:
                print(temp.roll, temp.name, temp.marks)
                temp = temp.next

    elif ch == 7:
        break

    else:
        print("Invalid Choice")
