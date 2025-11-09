from collections import Counter 
def frequency(nums:list, target:int):
    cnt = Counter(nums)
    for key,val in cnt.items():
        print(key ,val)
    print(cnt[target])
    # last occurence
    for i in range( len(nums) ):
        if nums[i] == target :
            last_ind = i
    print("last index of it is",last_ind)


if __name__ =="__main__":
    arr= [10,5,10,15,10,5]
    frequency(arr, 10)