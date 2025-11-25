# Python3 program to find the row
# with maximum number of 1s

# Function that returns
# index of row with maximum
# number of 1s.
def rowWithMax1s(mat):
    R = len(mat)
    C = len(mat[0])
    max_row = -1
    row = 0
    col = C - 1

    # Move till we are inside the matrix
    while row < R and col >= 0:
        # If the current value is 0, move down to the next row
        if mat[row][col] == 0:
            row += 1
        # Else if the current value is 1, update max_row and move to the left column
        else:
            max_row = row
            col -= 1

    return max_row


# Driver Code
mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print("Index of row with maximum 1s is",
      rowWithMax1s(mat))