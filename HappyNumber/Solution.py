class Solution:
    def isHappy(self, n: int) -> bool:

        state: bool = True
        first = self.verify(n)
        print("first is "+str(first))

        walk: int = n
        print("walk is "+str(walk))
        counter = 0

        while state:
            if first == walk:
                counter += 1
            if (counter >= 2):
                state = False
                return False
            walk = self.verify(walk)
            print("walk is "+str(walk))
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
