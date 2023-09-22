class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for key, val in dict.items():
            if val > (len(nums) / 2):
                return key
# time complexity: O(n)
# space complexity: O(n)

'''
Approach 1: Sorting

If an element occurs more than n/2 times in the array (where n is the size of the array), it will always occupy the middle position when the array is sorted. Therefore, we can sort the array and return the element at index n/2.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
time complexity: O(nlog(n))
space complexity: O(1)

Approach 2: Moore Voting Algorithm

The intuition behind the Moore's Voting Algorithm is based on the fact that if there is a majority element in an array, it will always remain in the lead, even after encountering other elements.

Algorithm:

1. Initialize two variables: count and candidate. Set count to 0 and candidate to an arbitrary value.
2. Iterate through the array nums:
    a. If count is 0, assign the current element as the new candidate and increment count by 1.
    b. If the current element is the same as the candidate, increment count by 1.
    c. If the current element is different from the candidate, decrement count by 1.
3. After the iteration, the candidate variable will hold the majority element.

def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
'''
