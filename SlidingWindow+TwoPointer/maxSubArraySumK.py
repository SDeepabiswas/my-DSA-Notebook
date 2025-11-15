def maxSum(arr, k):
    n = len(arr)

    if n<=k:
        print("Invalid")
        return -1
    
    window_sum = sum(arr[:k])

    maxs = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        maxs = max(window_sum,maxs)

    return maxs



if __name__ == "__main__":
    arr = [5, 2, -1, 0, 3]
    k = 3
    print(maxSum(arr, k))