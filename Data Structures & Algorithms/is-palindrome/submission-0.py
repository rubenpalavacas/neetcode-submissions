class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non alpha-numeric characters
        cleaned = ''.join(c for c in s if c.isalnum()).lower()
        i, j = 0, len(cleaned) - 1

        while i != j and i < len(cleaned) - 1 and j > 0:
            if cleaned[i] != cleaned[j]:
                return False
            i += 1
            j -= 1

        return True