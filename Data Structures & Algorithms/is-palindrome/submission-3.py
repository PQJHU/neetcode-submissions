import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed_c = re.compile(r"[a-zA-Z0-9]")

        i,j = 0, len(s) -1
        while i<j:
            if not allowed_c.match(s[i]):
                i+=1
                continue
            if not allowed_c.match(s[j]):
                j-=1
                continue
            print(s[i],s[j])
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
