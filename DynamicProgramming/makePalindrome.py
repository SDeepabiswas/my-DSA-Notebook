def findMinIsertions(s):

    n = len(s)
    dp = [0]* n

    # iterating over right to left
    for l in range (n-2,-1,-1):

        prev = 0
        # previous means dp[l+1][h-1] value, like er theke boro string er jonno

        for h in range(l+1, n):
            temp = dp[h]
            # storing before i overwrite

            if s[l] == s [h]:
                # no new insertions needed
                dp[h] = prev
            else:
                # i will take the min of two cases + 1

                dp[h] = min(dp[h] , dp[h-1]) +1

            prev = temp
    return dp[n-1]

if __name__ == "__main__":

    s = "adbac"
    print(findMinIsertions(s))
