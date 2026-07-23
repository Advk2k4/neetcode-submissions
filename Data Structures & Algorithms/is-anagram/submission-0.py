class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = []
        lst2 = []
        for i in s:
            lst1.append(i)
        lst1.sort()
        for j in t:
            lst2.append(j)
        lst2.sort()
        if lst1 == lst2:
            return True
        else:
            return False

