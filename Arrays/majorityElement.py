#   boyer-moore voting algorithm

# we search fr candidates of the majority element

# this is an O(n) time complexity and O(1) space complexity algorithm

def majorityELement(a):
    n = len(a)

    count = 0
    candidate = -1

    # find the candidate

    for val in a:
        if count == 0:
            candidate = val
            count = 1
        elif val == candidate:
            count +=1 
        else:
            count -= 1

    # validate the candidate

    count = 0
    for val in a:
        if val == candidate:
            count += 1
    
    # if the count is greater than n/2

    # candidate should de greater than n/2
    # else no majority element

    if count > n // 2:
        return candidate
    else:
        return -1

if __name__ == "__main__":
    
    arr = [2, 2, 2,2, 2, 1, 3, 5, 1]
    print(majorityELement(arr))        