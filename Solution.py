from typing import List

# Definición de la clase
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        k = 1

        while index < len(nums):
            value = nums[index]
            if value == nums[index - 1]:
                nums.pop(index)
            else:
                index += 1
                k += 1

        print(k)
        print(nums)
        return k

# Crear un objeto de la clase
sol = Solution()

# Lista de prueba
nums = [0,0,1,1,1,2,2,3,3,4]

# Llamar al método
k = sol.removeDuplicates(nums)

# k ya tiene el número de elementos únicos
print("Número de elementos únicos:", k)
print("Lista modificada:", nums)
