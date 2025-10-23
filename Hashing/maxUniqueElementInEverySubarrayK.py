# A is my array
#  k is the subarray size
#  we need to find the maximum unique element in each of the subarray of size k
def find_max(A,k):
    # this will store the count of each element, 
    # hashing sort of
    count = dict()
    
    # storing the count of first k-1 elements
    for i in range (k-1):
        count[A[i]] = count.get(A[i],0) + 1
    
    # avl tree can be used instead

    myset = dict()
    # storing the unique elements till k-1 only

    for x in count:
        if count[x] == 1:
            myset[x] = 1
    
    # SLIDING WINDOW APPROACH:
        # add one from right and delete one from left after done processing
    N = len(A)
    for i in range (k-1, N):

        count[A[i]] = count.get(A[i],0)+1

        if(count[A[i]] == 1):
            myset[A[i]] = 1

        else:
            del(myset[A[i]])

        if (len(myset) ==0 ):
            print("Nothing")
        
        else:
            maxm = -10**9
            for i in myset:
                maxm = max(i,maxm)
            print(maxm)

        # remove first element (sliding window)

        x = A[i-k+1]

        if x in count.keys():
            count[x] -=1
            if(count[x] == 1):
                myset[x] = 1
            if(count[x] == 0):
                del myset[x]

if __name__=="__main__":
    a = [3, 3, 3, 4, 4, 2 ]
    k = 4
    find_max(a, k)