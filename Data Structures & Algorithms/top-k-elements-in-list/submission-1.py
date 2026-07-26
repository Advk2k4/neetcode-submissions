class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] +=1

        buckets = [[] for s in range(len(nums)+1)]
        for n, freq in count.items():
            buckets[freq].append(n)

        res = []
        for q in range(len(buckets) -1, 0, -1):
            for m in buckets[q]:
                res.append(m)
                if len(res) == k:
                    return res