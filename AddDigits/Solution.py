class Solution:
    def addDigits(self, num: int) -> int:

        evaluate:bool=True
        aux = self.returnSum(num)
        while evaluate:
            if aux // 10 ==0:
                evaluate = False
                return aux
            else:
                aux = self.returnSum(aux)

        

        
    def returnSum(self,number) -> int:
        sum = 0
        while number >0:
            modul = number % 10
            # print("modul")
            # print(modul)
            number = number//10
            # print("number")
            # print(number)
            sum = sum+modul
            # print("sum")
            # print(sum)
        return sum

result = Solution()

# print(result.addDigits(38))
print(result.addDigits(15))
# print(result.addDigits(0))