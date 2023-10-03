class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''
        num_counts = {}
        good_pairs = 0

        # Count the occurrences of each number
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        
        # Calculate the number of good pairs for each number and sum them up
        for count in num_counts.values():
            good_pairs += count * (count - 1) // 2
    
        return good_pairs
        '''
        res = 0
        for i in range(len(nums)):
            if nums[i] in nums[i+1: ]:
                res += nums[i+1: ].count(nums[i])
        return res
