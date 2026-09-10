class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i, temp in enumerate(temperatures):
            current = 0
            print(i,temp)

            while stack:
                index = stack.pop()
                current = temperatures[index]
                if temp > current:
                    # This is the warmer day from the future
                    result[index] = i - index
                else: 
                    break
            
            stack.append(i)

        return result