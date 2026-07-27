class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = 0
        while n < len(s):
            m = n
            while s[m] != "#":
                m += 1
            length = int(s[n:m])
            res.append(s[m+1:m+1+length])
            n = m + 1 + length
        return res