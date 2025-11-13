from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #    from collections import deque
        dq = deque()  # will store indices
        ans = []

        for i in range(len(nums)):
        # Remove elements out of this window
            if dq and dq[0] == i - k:
                dq.popleft()

        # Remove all smaller elements (they’re useless)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

        # Once we've processed first k elements, start adding results
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans
    


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solution = Solution()
    print(solution.maxSlidingWindow(nums, k))