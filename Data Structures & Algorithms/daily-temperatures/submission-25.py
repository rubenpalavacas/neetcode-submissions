class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i, temp in enumerate(temperatures):
            current = 0
            greater = False

            while temp > current and stack:
                index = stack.pop()
                current = temperatures[index]
                
                if temp <= current:
                    stack.append(index)
                    break

                # This is the warmer day from the future
                result[index] = i - index
            
            stack.append(i)
            
        return result