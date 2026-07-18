class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if seen.get(dif) != None:
                return list([seen[dif],i])
            else:
                seen[nums[i]] = i
        
        return list([1,1])