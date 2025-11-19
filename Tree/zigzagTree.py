import createTree as tree
def zigZagTraversal(root):
    res = []
    if root is None:
        return res
    
    # Current level
    s1 = []
    
    # Next level
    s2 = []

    s1.append(root)

    while s1 or s2:

        # Print nodes of current level from s1
        # and push nodes of next level to s2
        while s1:
            curr = s1.pop()
            res.append(curr.data)
            
            if curr.left:
                s2.append(curr.left)
            if curr.right:
                s2.append(curr.right)

        # Print nodes of current level from s2
        # and push nodes of next level to s1
        while s2:
            curr = s2.pop()
            res.append(curr.data)
            
            if curr.right:
                s1.append(curr.right)
            if curr.left:
                s1.append(curr.left)
    return res

if __name__ == "__main__":
    
    # Create a input binary tree (this shall be modified later by a cleaner version)
    root = tree.Node(20)
    root.left = tree.Node(8)
    root.right = tree.Node(22)
    root.right.right = tree.Node(11)
    root.left.left = tree.Node(4)
    root.left.right = tree.Node(12)
    root.left.right.left = tree.Node(10)
    root.left.right.right = tree.Node(14)

    res = zigZagTraversal(root)
    for val in res: print(val, end=" ")
    print()