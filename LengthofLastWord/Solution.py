class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size = 0

        words = list(s)

        sizearray = len(words)-1
        for i in range(sizearray,-1,-1):
            character = words[i]
            if character != " ":
                size+=1
                if words[i-1] ==" ":
                    return size

        return size

a = Solution()
print(a.lengthOfLastWord("Hello World"))
print(a.lengthOfLastWord("   fly me   to   the moon  "))
print(a.lengthOfLastWord("luffy is still joyboy"))