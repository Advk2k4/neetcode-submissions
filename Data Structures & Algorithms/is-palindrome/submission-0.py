class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in range(len(s)):
            if s[i].isalnum():
                st += s[i].lower()
        if st == st[::-1]:
            return True
        else:
            return False