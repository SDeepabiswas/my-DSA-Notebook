# python3 Code For Boolean Matrix Question
# Most Optimised Approach
def booleanMatrix(mat):
    col0 = 0
    rows = len(mat)
    cols = len(mat[0])

    # Step 1: Mark the first row and column
    # if there is a 1 in the matrix
    for i in range(rows):
      
        # Check if 0th column contains 1
        if mat[i][0] == 1:
            col0 = 1  
        for j in range(1, cols):
            if mat[i][j] == 1:
                mat[i][0] = 1  
                mat[0][j] = 1  

    # Step 2: Traverse the matrix in reverse
    # direction and update values
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, 0, -1):
            if mat[i][0] == 1 or mat[0][j] == 1:
                mat[i][j] = 1  
        if col0 == 1:
            mat[i][0] = 1 

if __name__ == "__main__":
    arr = [
        [1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    
    booleanMatrix(arr)
    
    for row in arr:
        print(" ".join(map(str, row)))