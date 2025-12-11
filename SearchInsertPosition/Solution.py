from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            medium = (left+right) // 2

            if left == right:
                print("the last position is "+str(medium))
                if nums[medium] < target:
                    return medium+1
                else:
                    return medium

            if nums[medium] == target:
                return medium
            elif nums[medium] < target:
                left += 1
            else:
                right -= 1


r = Solution()
print(r.searchInsert([1, 3, 5, 6], 4))
