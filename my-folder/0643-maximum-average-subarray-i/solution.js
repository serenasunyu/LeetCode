/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    // let maxSum = -Infinity;
    // let windowSum = 0;

    // for (let i = 0; i < k; i++) {
    //     windowSum += nums[i];
    // }

    // maxSum = windowSum;

    // for(let i = k; i < nums.length; i++) {
    //     windowSum += nums[i] - nums[i - k];
    //     maxSum = Math.max(maxSum, windowSum)
    // }

    let sum = nums.slice(0, k).reduce((acc, num) => acc += num)
    let maxSum = sum;

    for(let i = k; i < nums.length; i++) {
        sum += nums[i] - nums[i - k];
        maxSum = Math.max(maxSum, sum);
    }
    return maxSum/k;
};
