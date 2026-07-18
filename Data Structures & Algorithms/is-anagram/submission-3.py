class Solution:
    # Could be done with several one-liners, but it would break the entire purpose of doing this.
    # Used the NeetCode video to get the definitive solution
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqs_s, freqs_t = {}, {}

        for i in range(len(s)):
            freqs_s[s[i]] = 1 + freqs_s.get(s[i],0)
            freqs_t[t[i]] = 1 + freqs_t.get(t[i],0)

        for c in freqs_s:
            if freqs_s[c] != freqs_t.get(c,0):
                return False

        return True
            
