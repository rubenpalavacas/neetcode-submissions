class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operations = { 
            "+": lambda a, b: a + b, 
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for token in tokens:
            if token not in operations:
                nums.append(int(token))
            else:
                b, a = nums.pop(), nums.pop()
                nums.append(operations[token](a,b))
        
        return nums.pop()