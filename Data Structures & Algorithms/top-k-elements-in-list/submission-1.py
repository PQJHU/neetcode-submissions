class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = {}
        for num in nums:
            counter_dict[num] = counter_dict.get(num, 0) + 1

        top_k_nums = sorted(counter_dict.keys(), key=counter_dict.get, reverse=True)[:k]
        return top_k_nums