class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = set(nums)
        l1 = len(nums)
        l2 = len(nums2)
        if l1 == l2:
            return False
        else:
            return True