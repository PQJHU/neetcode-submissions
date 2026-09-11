class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        The reverse polish notation follows the rule of
        1. reading left from right
        2. execute operation on the most recent two numbers as operands when meeting operator
        3. result from operation will be saved for next operation or output
        """
        operation_mapping = {
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
            "-": lambda x, y: x - y,
            "/": lambda x, y: int(x/y),
        }

        operand_stack = []
        for notation in tokens:
            if notation in ("+", "-", "*", "/"):
                _arg1, _arg2 = operand_stack.pop(), operand_stack.pop()
                _res = operation_mapping[notation](_arg2, _arg1)
                operand_stack.append(_res)
            else:
                operand_stack.append(int(notation))

        return operand_stack[-1]
