class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record_map = dict()
        if len(s) != len(t):
            return False
        for letter in s:
            record_map[letter] = record_map.get(letter, 0) + 1
        for letter in t:
            if letter not in record_map:
                return False
            record_num = record_map[letter]
            if record_num == 0:
                return False
            record_map[letter] = record_num - 1
        non_matached = [key for key in record_map if record_map[key] != 0]
        if len(non_matached) >0:
            return False
        return True
        