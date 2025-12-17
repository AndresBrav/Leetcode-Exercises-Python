class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tlist = list(t)
        slist = list(s)

        if len(slist) and len(tlist) >0:

            i = 0
            while i < len(slist):
                letter = slist[i]
                if letter in tlist: 
                    tlist.remove(letter)
                    slist.pop(i)
                else:
                    i+=1

            
            
            if len(tlist)==0 and len(slist)==0:
                return True
            else:
                return False
        else:
            return False



a = Solution()
print(a.isAnagram("ab", "a"))
print(a.isAnagram("anagram", "nagaram"))
print(a.isAnagram("rat", "car"))