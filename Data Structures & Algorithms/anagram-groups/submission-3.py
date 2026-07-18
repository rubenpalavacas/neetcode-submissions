class Solution:
    """Trying a more efficient solution using counts and hashing"""
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for str in strs:
            counts = [0] * 26 

            for c in str:
                counts[ord(c) - ord('a')] += 1
            
            # Remember to use tuple( --- ) when trying to use
            # a list as the key of a hash_map
            hash_map[tuple(counts)].append(str)

        return list(hash_map.values())
        