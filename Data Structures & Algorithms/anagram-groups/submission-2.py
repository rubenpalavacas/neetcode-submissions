class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            # The sort of the string is the key to group them
            sorted_str = self.sort_string(str)
            groups[sorted_str].append(str)

        return list(groups.values())

    def sort_string(self, s: str) -> str:
        #Trick found from https://www.geeksforgeeks.org/dsa/sort-string-characters/
        return ''.join(sorted(s))
