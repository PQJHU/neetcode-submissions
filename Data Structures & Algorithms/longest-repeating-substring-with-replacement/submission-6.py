class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 1
        max_len = 1
        freq_records = dict()
        freq_records[s[left]] = 1
        most_freq_c = s[left]

        while right < len(s):

            left_c, right_c = s[left], s[right]
            # append the right c in the record
            freq_records[right_c] = freq_records.get(right_c, 0) + 1
            most_freq_c = right_c if freq_records.get(right_c) > freq_records.get(most_freq_c) else most_freq_c
            if right - left + 1 - freq_records[most_freq_c] <= k:
                # valid
                right += 1
                max_len += 1
            else:
                # invalid
                freq_records[left_c] = freq_records[left_c] - 1
                left += 1
                right += 1

            # check the most freq c


        return max_len
