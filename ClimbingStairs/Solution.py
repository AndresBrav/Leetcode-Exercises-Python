class Solution:
    def climbStairs(self, n: int) -> int:
        number1 = 3
        number2 = 2
        n3=0

        if(n<4):
            return n
        else:
            for i in range(4,n+1):
                n3 = number1+number2
                number2=number1
                number1=n3

        return n3

res = Solution()
print(res.climbStairs(7))

