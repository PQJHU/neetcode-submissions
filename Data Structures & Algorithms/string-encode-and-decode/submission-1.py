class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = "#"
        return "".join([f"{len(string)}{sep}{string}" for string in strs])

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_str = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            str_len = s[i:j]
            decoded_str.append(s[j+1: j+ int(str_len)+1])
            i = j + int(str_len) + 1
        return decoded_str
