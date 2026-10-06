class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        We can use a slide window to explore s and see if the window cover t
        if not covered, move right pointer + 1
        if covered, move left pointer + 1
        Since we need to explore the minimum window, we need to record the window pos of the minimum window we explored
        To check if all chars in t are covered, we can use dict to record
        There is a few tricks:

        """
        res_left, res_right = -1, -1
        res_len = float("infinity")
        freq_t = dict()
        freq_window = dict()
        for c in t:
            # count t
            freq_t[c] = freq_t.get(c, 0) + 1

        covered = 0
        needed = len(freq_t)  # how many chars needed to be covered

        if needed == 0:
            return ""

        left, right = 0, 0
        while right < len(s):
            c_right = s[right]
            if c_right in freq_t:
                # add right char
                freq_window[c_right] = freq_window.get(c_right, 0) + 1

                if freq_window[c_right] == freq_t[c_right]:
                    # coverage increase only when the window freq char reach t freq char for the first time
                    # if the char in the window that has already covered, a repeated one will not increase the coverage
                    covered += 1

            while covered == needed:
                # shrinking, with fixed right pointer, until covered is broken
                c_left = s[left]
                if c_left in freq_t:
                    freq_window[c_left] = freq_window[c_left] - 1

                    if freq_window[c_left] < freq_t[c_left]:
                        # lose cover
                        covered -= 1
                        # when loosing coverage, c_left is the char that keeps the minimum window for the fixed right_c
                        if right - left + 1 < res_len:
                            res_left, res_right = left, right
                            res_len = right - left + 1
                left += 1

            # not fully covered, exploring
            right += 1

        return s[res_left: res_right + 1] if res_len is not float('infinity') else ""
