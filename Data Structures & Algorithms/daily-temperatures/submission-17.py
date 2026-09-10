class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i, temp in enumerate(temperatures):
            kept = []

            while value := stack.pop():
                if temp > value[0]:
                    # Warmer day
                    result[value[1]] = i - value[1]
                else:
                    kept.append(value)

            kept.append((temp,i))
            stack = kept



        return result