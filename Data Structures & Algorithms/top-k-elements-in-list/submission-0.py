class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = {}
        for num in nums:
            counter_dict[num] = counter_dict.get(num, 0) + 1

        max_k_freq = sorted([val for val in counter_dict.values()], reverse=True)[:k]
        top_k_nums = [key for key in counter_dict if counter_dict[key] in max_k_freq]

        return top_k_nums
        