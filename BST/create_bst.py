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



def delete_Node(root, key):
    if root is None:
        return root
    if root.value >key:
        root.left = delete_Node(root.left, key)
    elif root.value < key:
        root.right = delete_Node(root.right, key)
    else:
        # root has NO CHILDREN
        #  ONE CHILD
        if root.left is None:    
            return root.right
        if root.right is None:
            return root.left
                
        # TWO CHILDREN
        succ = getSuccessor(root)
        root.value = succ.value
        root.right = delete_Node(root.right, succ.value)
    
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
    # print("Found" if search(r, 19) else "Not Found")
    # print("Found" if search(r, 80) else "Not Found")
