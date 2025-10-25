#  there is a rod of length n, and a list of its price[i]
# the price of rod of length i+1
# we want to maximize the total selling price

# UNBOUNDED KNAPSACK PROBLEM

def cutRod(price):
    n = len(price)

    dp = [0] * (n+1)

    # our convention is dp[i] is the maximum
    # profit obtainable from rod length i 
    # in each iteration
    #  we check if the best profit for rod length i is 
    #  the current best or best of price of first cut + remaining's best

    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] = max(dp[i], price[j-1] + dp[i-j])
    return dp[n]


if __name__ == "__main__":
    # price = [1, 5, 8, 9, 10, 17, 17, 20]
    price = [3, 5, 8, 9, 10, 17, 17, 20]
    print(cutRod(price))