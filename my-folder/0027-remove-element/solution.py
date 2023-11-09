class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # # Initialize a variable k to keep track of elements not equal to val
        k = 0

        # Iterate through the nums array
        for i in range(len(nums)):

            # If the current element is not equal to val
            if nums[i] != val:

                # Move the current element to the position of the first occurrence of val
                nums[k] = nums[i]

                # Increment k to maintain the count of elements not equal to val
                k += 1
        
         # The first k elements in nums now contain elements not equal to val
        # k represents the number of elements in nums which are not equal to val
        return k

