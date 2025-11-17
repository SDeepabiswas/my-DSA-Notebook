# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Define a function to create a new Node
def newNode(key: int) -> Node:
    temp = Node(key)
    temp.left = temp.right = None
    return temp
