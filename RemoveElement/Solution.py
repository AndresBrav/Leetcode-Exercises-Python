from typing import List


class Solution:
    """
    Solution of the problem
    """

    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)  # remove this index
            else:
                i += 1       # we just advanced if we did not pop

        print(len(nums))
        return len(nums)


sol = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
sol.removeElement(nums, val)
print(nums)
