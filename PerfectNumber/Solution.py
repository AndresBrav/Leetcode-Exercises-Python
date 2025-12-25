class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = False
        first = 0
        second = 0
        p = 2
        run = True

        while run:
            first = 2 ** (p - 1)
            # print(first)
            second = (2**p) - 1
            # print(second)
            multi = first * second
            # print(multi)
            if self.is_prime(second):
                if multi == num:
                    return True
                if multi > num:
                    run = False
            p += 1
        return res

    def is_prime(self, number):
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False

        limit = int(number**0.5) + 1  # Calcula la raíz cuadrada sin usar math
        for i in range(3, limit, 2):
            if number % i == 0:
                return False

        return True


a = Solution()
print(a.checkPerfectNumber(6))
print(a.checkPerfectNumber(496))
print(a.checkPerfectNumber(8128))
print(a.checkPerfectNumber(1))
print(a.checkPerfectNumber(7))
