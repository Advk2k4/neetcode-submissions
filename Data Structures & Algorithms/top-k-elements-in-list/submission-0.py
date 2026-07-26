class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        sort_freq = sorted(freq.items(), key = lambda item: item[1], reverse = True)
        return [pair[0] for pair in sort_freq[0:k]]