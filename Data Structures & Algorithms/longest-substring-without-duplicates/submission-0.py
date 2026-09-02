class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub_string_record = set()
        sub_string = deque()
        sub_string_len = 0
        for char in s:
            if char not in sub_string_record:
                sub_string.append(char)
                sub_string_record.add(char)
                sub_string_len += 1
                # max_len = max(len(sub_string), max_len)
                max_len = max(sub_string_len, max_len)
            else:
                while sub_string:
                    # remove the chars up until the dup char
                    popped_char = sub_string.popleft()
                    sub_string_record.remove(popped_char)
                    sub_string_len -= 1
                    if popped_char == char:
                        break
                # add the dup/new char
                sub_string_record.add(char)
                sub_string.append(char)
                sub_string_len += 1
        return max_len
        