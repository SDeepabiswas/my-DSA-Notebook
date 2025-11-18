class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def newNode(key: int):
    return Node(key)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# Example usage
if __name__ == "__main__":
    root = newNode(10)
    root.left = newNode(5)
    root.right = newNode(15)
    inorder(root)
