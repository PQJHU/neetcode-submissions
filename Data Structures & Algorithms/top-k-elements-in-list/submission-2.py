class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        count = Counter(nums)  # the same as using counter_dict

        top_k = heapq.nlargest(k, count, count.get)
        return top_k

