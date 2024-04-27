/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    let left = 0;
    let right = 0;
    let maxOnesCount = 0;
    let zeroCount = 0;

    while(right < nums.length) {
        if (nums[right] === 0) {
            zeroCount++;
        }
    
        // Shrink the window if the zero count exceeds k
        while(zeroCount > k) {
            if(nums[left] === 0) {
                zeroCount--;
            }
            left++;
        }
        // Update the maximum ones count
        maxOnesCount = Math.max(maxOnesCount, right - left + 1);

        // Move the right pointer to expand the window
        right++;
    }
    return maxOnesCount;
};
