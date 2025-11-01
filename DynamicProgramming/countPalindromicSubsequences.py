def countPS(s):
    l = len(s)
    dp = [ [0] * l for _ in range (l)]
    for i in range(l):
        dp[i][i] = 1
        # single letters are always palindromes

    # i count palindromes for each substrings of length i
    for i in range (2,l+1):
        # i length substrings starting from j
        for j in range (l-i+1):
            # calculating the corresponding ending index
            k = j + i - 1
            if s[j] == s[k]:
                dp[j][k] = dp[j+1][k] + dp[j][k-1] + 1
            else:
                dp[j][k] = dp[j+1][k] + dp [j][k-1] - dp[j+1][k-1]
            
    
    return dp [0][l-1]

if __name__ =="__main__":
    s = "leetcode"
    s2 = "geeksforgeeks"
    print(countPS(s2))

 
