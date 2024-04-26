class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        maxCount = 0
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        maxCount = max(maxCount, count)
        
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1

            maxCount = max(maxCount, count)

        return maxCount
