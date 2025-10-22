import create_bst as bst

# MORRIS TRAVERSAL 
def preorder(root):
    res = []
    while root:
        # current node has no left child
        if root.left is None:
            res.append(root.value)
            root = root.right
        # current node has a left child
        else:

            # finding inorder predeccessor
            curr = root.left
            # finding rightmost node in the left subtree
            while curr.right and curr.right !=root:
                curr = curr.right

            # if the right child of inorder predecessor 
            # already points to this node
            if curr.right == root:
                curr.right = None
                root = root.right

            # if right child doesn't point to this node then print this
            # node and make right child point to this node
            else:
                res.append(root.value)
                curr.right = root
                root = root.left
    return res
    
# temporarily connect a node's predecessor's right child to the current node


if __name__ == "__main__":
    r = bst.Node(50)
    r = bst.insert(r, 60)
    r = bst.insert(r, 70)
    res = preorder(r)

    for i in res:
        print(i, end=" ")
    

