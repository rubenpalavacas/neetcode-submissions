from heapq import heappop, heappush, heapify

class Solution:
    """
    Heap-style solution ( O(k))
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # We count negative to turn the min heap into a max heap
        for num in nums:
            count[num] = -1 + count.get(num,0)

        # Value is the frequency that we want to use as max-heap key
        count_list = list(zip(count.values(),count.keys())) 
        heapify(count_list)
        res = []

        for i in range(k):
            pair = heappop(count_list)
            res.append(pair[1])
            
        return res
            

