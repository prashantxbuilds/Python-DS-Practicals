
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


prefix = "+--a*bc/def"
stack = []

# Construct Expression Tree
for ch in prefix[::-1]:
    newNode = Node(ch)

    if ch in "+-*/":
        newNode.left = stack.pop()
        newNode.right = stack.pop()

    stack.append(newNode)

root = stack.pop()

# Non-Recursive Postorder Traversal
s1 = [root]
s2 = []

while s1:
    temp = s1.pop()
    s2.append(temp)

    if temp.left:
        s1.append(temp.left)

    if temp.right:
        s1.append(temp.right)

print("Postorder Traversal:", end=" ")

while s2:
    print(s2.pop().data, end=" ")

# Delete Entire Tree
delete_stack = [root]

while delete_stack:
    temp = delete_stack.pop()

    if temp.left:
        delete_stack.append(temp.left)

    if temp.right:
        delete_stack.append(temp.right)

    temp.left = None
    temp.right = None

root = None

print("\nEntire Expression Tree Deleted!")
