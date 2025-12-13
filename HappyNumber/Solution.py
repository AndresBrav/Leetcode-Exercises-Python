class Solution:
    def isHappy(self, n: int) -> bool:

        state: bool = True
        numberList: list[int] = []
        walk: int = n
        print("walk is "+str(walk))

        while state:
            walk = self.verify(walk)
            numberList.append(walk)
            print("walk is "+str(walk))
            repeatcantity = numberList.count(walk)
            if (repeatcantity > 1):
                state = False
                return False

            if (walk == 1):
                state = False
                return True

    def verify(self, n: int) -> int:
        state: bool = True
        number: int = n
        sum = 0
        while state:
            if (number == 0):
                state = False
                print("reached the limit")
                return sum
                print("sum es"+str(sum))
            else:
                mod = number % 10
                # print("mod es"+str(mod))
                number = number // 10
                # print("num es"+str(number))
                sum = sum + mod**2
                # print("sum es"+str(sum))


a = Solution()
print(str(a.isHappy(256)))
