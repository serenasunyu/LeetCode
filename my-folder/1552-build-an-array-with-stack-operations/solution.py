class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # # Initialize an empty list to store the operations
        operations = []
        # # Initialize a pointer to keep track of the current position in the target array
        target_ptr = 0

        for num in range(1, n+1):
            # If the current number matches the next number in the target array
            if target_ptr < len(target) and num == target[target_ptr]:
                operations.append("Push")
                # Move the target pointer to the next element in the target array
                target_ptr += 1
            else:
                # If the current number is not in the target array
                operations.append("Push")
                operations.append("Pop")

        # If all elements in the target array have been processed, stop the loop
            if target_ptr == len(target):
                break
    
        return operations


