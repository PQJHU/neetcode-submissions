class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = "@"
        encoded_str = ""
        for string in strs:
            encoded_str += f"{sep}{len(string)}_{string}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        sep = "@"
        decoded_strs = []
        c_idx = 0
        while c_idx < len(s):
            c = s[c_idx]
            if c == sep:
                string_len = ""
                for k in range(1, 4):
                    if s[c_idx + k] == "_":
                        break
                    string_len += s[c_idx + k]
                string_offset = int(string_len)
                mark_offset = len(string_len) + 2
                # normal encoded case, @ is used only for string separation
                decoded_strs.append(s[c_idx + mark_offset:c_idx+ mark_offset+ string_offset])
                c_idx += mark_offset + string_offset
        return decoded_strs
