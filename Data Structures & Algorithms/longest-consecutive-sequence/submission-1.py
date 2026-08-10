class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0

        for num in nums:
            # This is the KEY: check for direct LEFT neighbour to check start of sequence.
            if (num - 1) not in nums_set:
                # From here, just do what i had deduced: look for a sequence starting in that num.
                sequence = 0
                while ( num + sequence ) in nums_set:
                    sequence += 1
                # Keep track of the biggest sequence seen, and return it. 
                longest_sequence = max(longest_sequence,sequence)
            

        return longest_sequence