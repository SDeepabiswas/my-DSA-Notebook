# Python program to find out the maximum length
# of a side of a square sub-matrix with all 1s.

def maxSquare(mat):
    n, m = len(mat), len(mat[0])
    ans = 0

    # Create 1d array
    dp = [0] * (n + 1)

    # variable to store the value of 
    # {i, j+1} as its value will be 
    # lost while setting dp[i][j+1].
    diagonal = 0

    # Traverse column by column
    for j in range(m - 1, -1, -1):
        for i in range(n - 1, -1, -1):
            tmp = dp[i]

            # If square cannot be formed
            if mat[i][j] == 0:
                dp[i] = 0
            else:
                # minimum of the three neighboring cells
                
                dp[i] = 1 + min(dp[i], diagonal, dp[i + 1])

            diagonal = tmp
            ans = max(ans, dp[i])

    return ans

if __name__ == "__main__":
    mat = [
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    print(maxSquare(mat))