class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


def insert(root,key):
    if root is None:
        return Node(key)
    if root.value == key:
        return root
    if root.value < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left , key)
    return root



def search(root, key):
    if root is None or root.value == key :
        return root
    if root.value < key:
        return search(root.right, key)
    else:
        return search(root.left, key)
    


def getSuccessor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def detach_successor(node):
    if node.right is None:
        return None, node.right

    parent = node
    child = node.right
    # if right child has no ;eft child then it is the successor

    if child.left is None:
        parent.right = child.right
        return child, node.right

    # go as much left as possible

    while child.left is not None:
        parent = childchild = child.left

    # ?detach the getSuccessor
    parent.left = child.right
    return child, node.right


def delete_Node(root, key):
    if root is None:
        return root
    
    if root.value >key:
        root.left = delete_Node(root.left, key)
    elif root.value < key:
        root.right = delete_Node(root.right, key)
    else:
        # two children case
        successor, new_right = detach_successor(root)
        if successor is not None:
            root.value = successor.value
            root.right = new_right
        else:
            child = root.left if root.left else root.right
            root = None
            return child
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value,end=" ")
        inorder(root.right)
        
# if __name__ == "__main__":
#     r = Node(50)
#     r = insert(r, 30)
#     r = insert(r, 20)
#     r = insert(r, 40)
#     r = insert(r, 70)
#     r = insert(r, 60)
#     r = insert(r, 80)

#     x = 20

#     delete_Node(r, 80)
#     inorder(r)
#     print("Found" if search(r, 19) else "Not Found")
#     print("Found" if search(r, 60) else "Not Found")
