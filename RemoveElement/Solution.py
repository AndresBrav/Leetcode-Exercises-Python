from typing import List


class Solution:
    """
    Solution of the problem
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i = i+1
        print(len(nums))
        return len(nums)


sol = Solution()
nums = [3, 2, 2, 3]
val = 3
sol.removeElement(nums, val)
print(nums)
