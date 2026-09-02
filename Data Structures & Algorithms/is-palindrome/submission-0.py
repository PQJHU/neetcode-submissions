class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        allowed_c = re.compile(r"[a-zA-Z0-9]")
        clean_s = [c.lower() for c in s if allowed_c.match(c)]
        i, j = 0, len(clean_s) -1
        while i<j:
            if clean_s[i] != clean_s[j]:
                return False
            i += 1
            j -= 1
        return True
        