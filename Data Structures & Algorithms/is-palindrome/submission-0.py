class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(i for i in s.lower() if i.isalnum())
        return s1 == s1[::-1]
        