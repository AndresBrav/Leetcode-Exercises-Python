class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # print(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
        iterator= True

        zeros = nums.count(0)

        counter = 0
        i=0
        while iterator:
            # print("size of array is "+str(len(nums)))
            if(nums[i]==0):
                nums.pop(i)
                counter +=1
                if counter ==zeros:
                    iterator = False
                    for x in range(zeros):
                        nums.append(0)
                
            else:
                i+=1

        print(nums)


a = Solution()
# a.moveZeroes([0])
a.moveZeroes([0,1,0,3,12])