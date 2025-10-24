import create_bst as bst
def insert(node, data):

    global succ

    root = node

    if (node == None):
        return bst.Node(data)

    # If key is smaller than root's key, go to left
    # subtree and set successor as current node
    if (data < node.value):

        succ = node
        root.left = insert(node.left, data)

    # Go to right subtree
    elif (data > node.value):
        root.right = insert(node.right, data)

    return root



# Function to replace every element with the
# least greater element on its right


def replace(arr, n):

    global succ
    root = None

    # Start from right to left
    for i in range(n - 1, -1, -1):
        succ = None

        # Insert current element into BST and
        # find its inorder successor
        root = insert(root, arr[i])

        # Replace element by its inorder
        # successor in BST
        if (succ):
            arr[i] = succ.value

        # No inorder successor
        else:
            arr[i] = -1

    return arr


if __name__ == '__main__':

    arr = [8, 58, 71, 18, 31, 32, 63,
           92, 43, 3, 91, 93, 25, 80, 28]
    n = len(arr)
    succ = None

    arr = replace(arr, n)

    print(*arr)