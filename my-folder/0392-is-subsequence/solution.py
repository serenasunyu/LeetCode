class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        i, j = 0, 0  # Pointers for s and t
    
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move s pointer if characters match
            j += 1  # Always move t pointer
            
        return i == len(s)  # If all characters in s were found, it's a subsequence
        '''
        # Dynamic Programming
        dp = [[False] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        # Base case: an empty string is always a subsequence of any string.
        for i in range(len(t) + 1):
            dp[0][i] = True
        
        # Fill the dp table based on matching characters.
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                # If the characters match, the subsequence status depends on the previous characters.
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # If characters don't match, subsequence status is the same as without the current character in s.
                else:
                    dp[i][j] = dp[i][j - 1]
        
        # If the last cell is True, s is a subsequence of t.
        return dp[len(s)][len(t)]




