from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(n):
            total += nums[right]  # expand the window
            
            # shrink window while sum >= target
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len


# ----------------------------
# Main function / test driver
# ----------------------------
if __name__ == "__main__":
    target = int(input("Enter target: "))
    nums = list(map(int, input("Enter array elements separated by space: ").split()))
    
    sol = Solution()
    result = sol.minSubArrayLen(target, nums)
    
    print("Minimum length of subarray:", result)
