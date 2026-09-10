class Solution:
    """
    Improvements made from NeetCode's solution
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                # This is the warmer day from the future
                result[stackIndex] = i - stackIndex
            stack.append([temp,i])
            
        return result