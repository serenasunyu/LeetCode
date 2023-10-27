class Solution:
    def longestPalindrome(self, s: str) -> str:
        # step1: preprocess the input string
        processed_str = "^#"
        for c in s:
            processed_str += c + "#"
        processed_str += "$"

        # step2: initialize variables for the algorithm
        str_length = len(processed_str)
        palindrome_lengths = [0] * str_length
        center = 0 # current center of the palindrome
        right_edge = 0 # rightmost edge of the palindrome

        # step3: loop through the modified string to find palindromes
        for i in range(1, str_length - 1):
            palindrome_lengths[i] = min(right_edge - i, palindrome_lengths[2 * center - i]) if right_edge > i else 0

            # expand the palindrome around the current character
            while processed_str[i + 1 + palindrome_lengths[i]] == processed_str[i - 1 - palindrome_lengths[i]]:
                palindrome_lengths[i] += 1

            # update the rightmost edge and center if necessary
            if i + palindrome_lengths[i] > right_edge:
                center = i
                right_edge = i + palindrome_lengths[i]
            
        # step4: find the longest palindrome and its center
        max_length = 0
        max_center = 0
        for i in range(str_length):
            if palindrome_lengths[i] > max_length:
                max_length = palindrome_lengths[i]
                max_center = i

        # step5: extract the longest palindrome from the modified string
        start = (max_center - max_length) // 2
        end = start + max_length

        # return the longest palindrome in the original string
        return s[start:end]
