class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        # for each possible freq, create a bucket, max of len(nums) freq

        for val, freq in count.items():
            buckets[freq].append(val)

        top_k = []
        for bucket_index in range(len(buckets)-1, 0, -1):
            for val in buckets[bucket_index]:
                top_k.append(val)
                if len(top_k) >= k:
                    return top_k
