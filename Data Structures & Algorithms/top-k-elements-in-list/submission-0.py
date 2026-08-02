class Solution:
    """
    Solution done following the NeetCode solution video :D
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [ [] for i in  range(len(nums) + 1 ) ]

        for num in nums:
            counts[num] = 1 + counts.get(num,0) # to guard against uninitialized values
        
        for num, count in counts.items():
            freq[count].append(num) # Adding the number to its corresponding frequency cell

        res = []

        for i in range(len(freq) - 1, 0, -1): 
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
