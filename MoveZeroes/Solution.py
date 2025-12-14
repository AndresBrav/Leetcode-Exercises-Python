class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        print(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        i=0
        iterator= True

        while i < len(nums):
            print("size of array is "+str(len(nums)))
            if(nums[i]==0):
                nums.pop(i)
                
            else:
                i+=1

        print(nums)


a = Solution()
a.moveZeroes([0,1,0,3,12])