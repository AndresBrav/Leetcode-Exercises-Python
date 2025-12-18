class Solution:
    def isUgly(self, n: int) -> bool:
        evaluate = True


        res = True

        if n<1:
            return False

        if n==1:
            return True

        while evaluate:
            if n % 2 ==0:
                n = n//2
                if n ==1:
                    evaluate = False
            elif n%3==0:
                n = n//3
                if n ==1:
                    evaluate = False
            elif n%5 ==0:
                n = n//5
                if n ==1:
                    evaluate = False
            else:
                res = False
                evaluate = False
        return res

a = Solution()
print(a.isUgly(14))
print(a.isUgly(1))
