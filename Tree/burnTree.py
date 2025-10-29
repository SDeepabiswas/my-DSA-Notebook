import createTree as tree

from typing import List, Dict


# we find the time to burn the tree. that is basically, dfs and find out how long can fire reach

def findMinTime(root: tree.Node, target: int, level: int,
                ans: Dict[int, List[int]], burnt: int) -> int:
    if root is None:
        return -1
    
    # NODE IS ALREADY BURNING
    # level essentially means the time step
    if burnt == 1:
        ans[level].append(root.data)

    # just FOUND the node to be BURNED 
    if root.data == target:
        ans[0].append(root.data)
        findMinTime(root.left, target, 1, ans, 1)
        findMinTime(root.right, target, 1, ans, 1)
        return 1

    # RECURSIVELY BURNN
    left = findMinTime(root.left, target, level+1, ans, burnt )
    right = findMinTime(root.right, target, level+1, ans, burnt)
    

    # fire in left subtree
    if left != -1:
        ans[left].append(root.data)
        findMinTime(root.right, target, left+1, ans,  1)
        return left +1
    

    # fire in right subtreee
    if right != -1:
        ans[right].append(root.data)
        findMinTime(root.left, target, right +1,ans,1)
        return right+1
    
    # NONE HAS FIRE
    return -1


def minTime(root: tree.Node, target: int) -> Dict[int, List[int]]:
    # Initialize an empty dictionary to store the answer
    ans = {i: [] for i in range(100)}
    # Call the recursive function to find the minimum time
    findMinTime(root, target, 0, ans, 0)
    # Return the answer dictionary
    return ans

# Driver code
if __name__ == '__main__':
    # Create the binary tree
    root = tree.newNode(10)
    root.left = tree.newNode(12)
    root.right = tree.newNode(13)

    root.right.left = tree.newNode(14)
    root.right.right = tree.newNode(15)

    root.right.left.left = tree.newNode(21)
    root.right.left.right = tree.newNode(22)
    root.right.right.left = tree.newNode(23)
    root.right.right.right = tree.newNode(24)
    
    # Set the target node
    targetNode = 14

    # Call the function to find the minimum time required to burn the binary tree
    answer = minTime(root, targetNode)

    # Print the answer
    for key, value in answer.items():
        if not value:
            break
        print(f"Nodes burnt at stage {key} are {value}")