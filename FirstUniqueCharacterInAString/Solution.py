class Solution:
    def firstUniqChar(self, s: str) -> int:
        listS = list(s)
        notEvalueate = []

        size = len(listS)
        i = 0
        x = size -1 
        res = -1
        while i < size:
            counter = 0
            while x >-1:
                if listS[i] ==listS[x]:
                    counter += 1

                if x ==0 and counter ==1:
                    return i
                
                if counter >1:
                    break

                x-=1
            x = size -1 
            i+=1


        return res
a = Solution()
print(a.firstUniqChar("leetcode"))
print(a.firstUniqChar("aabb"))
print(a.firstUniqChar("loveleetcode"))