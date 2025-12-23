class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s)>0:
            for i in range (len(s)):
                if s[i] != t[i]:
                    return t[i]
                if i == len(s)-1:
                    return t[len(s)]
        else:
            return t[len(s)]

res = Solution()
print(res.findTheDifference("abcd", "xabcde"))
print(res.findTheDifference("", "y"))