class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        num_counts = {}
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else: 
                num_counts[num] = 1
        res = []
        for num, cnt in num_counts.items():
            if cnt > len(nums)/3:
                res.append(num)
        return res

        # Create a Counter to store the count of each element
        element_count = Counter(nums)
        
        majority_elements = []
        threshold = len(nums) // 3
        
        # Iterate through the element count to identify majority elements
        for element, count in element_count.items():
            # Check if the element count is greater than the threshold
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements
        '''
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        
        # Step 1: Find potential candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Count the occurrences of potential candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        result = []
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)
        
        return result

