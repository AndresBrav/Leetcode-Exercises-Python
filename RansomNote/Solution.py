class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        listransomNote = list(ransomNote)
        listmagazine = list(magazine)
        res = True

        i = 0
        while len(listransomNote) > 0:
            # print("the size is "+str(len(listransomNote)))
            character = listransomNote[i]
            if character in listmagazine:
                listmagazine.remove(character)
                listransomNote.pop(i)
                
            else:
                return False
        
        
        return res

res = Solution()

# print(res.canConstruct("a","b"))
# print(res.canConstruct("aa","bb"))
print(res.canConstruct("aba","aa"))
# res.canConstruct("aa","bb")
# res.canConstruct("aa","aab")