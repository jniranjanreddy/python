class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub =""
        for i in range(2,len(s)+1):
            sub = s[0:i]
            if sub == sub[::-1]:
                print("palindromr")

t = Solution()
print(t.s)