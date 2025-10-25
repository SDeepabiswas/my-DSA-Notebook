# nth term is Cn = (2n)!/((n+1)!n!)
# APPLICATIONS:
# Count the number of expressions containing n pairs of parentheses that are correctly matched.
# Count the number of possible Binary Search Trees with n keys (See this)
# Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.
# Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that no 2 chords intersect.


# C0=C1=1 AND Cn =  summation of i = 0 to n - 1 CiCn-i-1 for n>=2

# the O(n) iterative algo for this is Cn = Cn-1 * (4n-2)/(n+1)

def findCatalan(n):
    catalan = [0] *(n+1)
    catalan[0] = catalan[1] = 1

    for i in range (2,n+1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan [i-j-1]
    
    return catalan[n]

if __name__ == "__main__":
    print(findCatalan(6))