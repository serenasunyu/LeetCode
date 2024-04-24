/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    let res = 0;
    nums.sort((a,b) => a-b); // sort the arry to use two pointer approach
    let i = 0;
    let j = nums.length -1;
    while(i < j) {
        if(nums[i] + nums[j] === k) {
            res += 1;
            i++;
            j--;
        } else if (nums[i] + nums[j] < k) {
            i++; // move left pointer to increase the sum
        } else {
            j--; // move right pointer to decrease the sum
        }
    }
    return res;
    
};
