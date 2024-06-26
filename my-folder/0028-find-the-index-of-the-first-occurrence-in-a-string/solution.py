class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # edge case: an empty string is considered to be found at the start of any string
        if not needle:
            return 0

        # Helper function computes the Longest Prefic Suffix array used to skip unnecessary comparisons
        def computeLPSArray(needle:str) -> list:
            lps = [0] * len(needle) # initailize LPS array with zeros
            length = 0 # length of the previous longest prefic and suffix
            i = 1 # start from the second character

            # loop through the needle to populate the LPS array
            while i < len(needle):
                if needle[i] == needle[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = computeLPSArray(needle)
        i = 0
        j = 0

        while i < len(haystack):
            if needle[j] == haystack[i]:
                i += 1
                j += 1

            if j == len(needle):
                return i - j
            elif i < len(haystack) and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
