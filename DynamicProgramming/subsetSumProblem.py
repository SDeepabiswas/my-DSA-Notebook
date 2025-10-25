# is a subset in an array exists with a given sum
# MEMORY EFFICIENT DP solution


def isSubsetSum(arr, sum):
    n = len(arr)

    # creating two boolean arrays

    prev = [False] * (sum+1)
    curr = [False] * (sum+1)

    # the both arrays represent whether a subset of first i - 1 
    # elements can make a sum of j prev[j]
    # for curr it is first i elements

    # base case: 0 sum can always be there

    prev[0] = True

    for i in range (1, n+1):
        for j in range (sum+1):
            if j < arr[i-1]:
                curr[j] = prev[j]
            else:
                curr[j] = prev[j] or prev[j - arr[i-1]]
        prev = curr.copy()

# everytime in each iteration we just need to check 
# if the addition of the current element can be allowed 
# given our upper bound is sum
    return prev[sum]


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum_value = 86
    if isSubsetSum(arr, sum_value):
        print("True")
    else:
        print("False")