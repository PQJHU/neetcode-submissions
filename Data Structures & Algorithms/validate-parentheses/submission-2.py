class Solution:
    def isValid(self, s: str) -> bool:
        open_mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack_list = []
        for p in s:
            if p in open_mapping.values():
                stack_list.append(p)
            elif p in open_mapping.keys():
                if len(stack_list) != 0 and open_mapping[p] == stack_list[-1]:
                    stack_list.pop()
                else:
                    return False
        if len(stack_list) != 0:
            return False

        return True
        