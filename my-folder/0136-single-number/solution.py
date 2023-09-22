class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {} 
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict.pop(i)
        return next(iter(dict))
