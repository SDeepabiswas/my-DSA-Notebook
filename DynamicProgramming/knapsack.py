# this is a 0/1 knapsack problem

def knapsack(W, val, wt):

    #  Initializing dp list
    dp = [0] * (W+1)

    # dp[w]is the maximum profit we can achieve with weight limit w
    
    # initially, all are 0, we cannot earn profit without any items
    #  we iterate through the items and decide if we allow it or skip it
    # taking the first i elements
    for i in range (1, len(wt) + 1):

        #Starting from back, so that we have data of 
        # previous computation of i-1 items

        for j in range(W, wt[i-1] - 1, -1):
            dp[j] = max(dp[j], dp[j - wt[i-1]] +val[i-1])

    return dp[W]
     
if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4

    print(knapsack(W, val, wt))