class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        for x in range(size):
            number = nums[x]
            # print(nums[x])
            cantity = nums.count(number)
            # print(cantity)
            if cantity > size//2:
                return number

a = Solution()
a.majorityElement([2,2,1,1,1,2,2])
# a.majorityElement([3,2,3])
