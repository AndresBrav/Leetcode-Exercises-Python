from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_ = 0
        i = 0
        e = len(digits) - 1

        while i < len(digits):
            aux = digits[i]
            sum_ = sum_ + aux * (10 ** e)
            i += 1
            e -= 1

        total_sum = sum_ + 1

        inverse = self.get_array_inverse(total_sum)

        res = list(reversed(inverse))

        print("the answer is :")
        print(res)
        return res

    def get_array_inverse(self, num: int) -> List[int]:
        inverse = []
        while num > 0:
            aux1 = num % 10
            inverse.append(aux1)
            num //= 10
        #print(inverse)
        return inverse


sol = Solution()
digits = [4,3,2,1]
sol.plusOne(digits)
