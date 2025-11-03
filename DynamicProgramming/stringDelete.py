# Function to find the minimum operations
# to delete the string entirely.
def minOperations(str):
    n = len(str)
    
    # create a 2d array dp[] to store
    # the results of subproblems
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # loop for substring length we are considering
    for L in range(1, n + 1):
        # loop with two variables i and j, denoting
        # starting and ending of substrings
        for i in range(0, n - L + 1):
            j = i + L - 1
            
            # If substring length is 1, then 1 step
            # will be needed
            if L == 1:
                dp[i][j] = 1
            else:
                # delete the ith char individually
                # and assign result for subproblem (i+1,j)
                dp[i][j] = 1 + dp[i + 1][j]
                
                # if current and next char are same,
                # choose min from current and subproblem
                # (i+2,j)
                if str[i] == str[i + 1]:
                    dp[i][j] = min(1 + dp[i + 2][j], dp[i][j])
                
                # find the index of the next character
                # which is same as the first character
                for k in range(i + 2, j + 1):
                    if str[i] == str[k]:
                        dp[i][j] = min(dp[i + 1][k - 1] + 
                        dp[k + 1][j], dp[i][j])
                        
    return dp[0][n - 1]

if __name__ == "__main__":
    str = "2553432"
    print(minOperations(str))