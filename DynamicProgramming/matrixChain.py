# top level multiplication how should we break it up

# you can use recursion or divide and conquer
# cost = min cost(1...k)+cost(k+1...m)
# this ends up recomputing the subproblems repeatedly


# BOTTOM UP APPROACH

# A1 X A2 X A3 
# two ways to compute
# A1 X A2, RES X A3, and the other

# at every position you are looking at what's the best way to do a chain of length 3 starting from that position
# at every position you are looking at what's the best way to do a chain of length 4 starting from that position
# .....

# find the minimum of cost[i,j] = cost[i,k] + cost[i+k, j-k] + NiNi+kNi+j
#  position is i and length of chain is j

def matrixMultiplication(arr):
    n = len(arr)

    # creating the 2d array to store 
    # minimum multiplication costs

    dp = [[0] * n for _ in range(n)]

# filling in the dp array
# length is the chain length here

    for length in range (2,n):
        for i in range(n-length):
            j = i + length
            dp[i][j] = float('inf')

            for k in range(i+1, j):
                cost = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j] , cost)

    
    return dp[0][n-1]

# 3 matrices of dimensions 2x1, 1x3, and 3x4, 
if __name__ == "__main__":
    arr = [3, 4]
    print(matrixMultiplication(arr))
