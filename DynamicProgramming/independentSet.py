# JUST GET A HANG OF THE IDEA OF INDEPENDENT SET IN A TREE

# A binary tree node has data,
# pointer to left child and a
# pointer to right child
class node:
    def __init__(self, data):
        
        self.data = data
        self.left = self.right = None
        self.liss = 0

# A memoization function returns size
# of the largest independent set in
# a given binary tree
def liss(root):
    
    if root == None:
        return 0
      
    if (root.liss):
        return root.liss
    
    if (root.left == None and 
        root.right == None):
        root.liss = 1
        return root.liss

    # Calculate size excluding the
    # current node
    liss_excl = (liss(root.left) + 
                 liss(root.right))

    # Calculate size including the
    # current node
    liss_incl = 1
    if root.left != None:
        liss_incl += (liss(root.left.left) + 
                      liss(root.left.right))
        
    if root.right != None:
        liss_incl += (liss(root.right.left) +
                      liss(root.right.right))
        
    # Maximum of two sizes is LISS,
    # store it for future uses.
    root.liss = max(liss_excl, liss_incl)
    
    return root.liss
    
# Driver Code

# Let us construct the tree given
# in the above diagram
root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)
root.right = node(22)
root.right.right = node(25)

print("Size of the Largest Independent "\
      "Set is ", liss(root))