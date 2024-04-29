/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    // two pointer

    // let max = 0;
    // let deleted = 0;
    // let l = 0;
    // let r = 0;

    // while(r < nums.length) {
    //     if(nums[r] === 1 || deleted === 0) {
    //         if(nums[r] === 0) deleted = 1;
    //         max = Math.max(max, r - l + 1 - deleted);
    //         r++;  
    //     } else {
    //         if(nums[l] === 0) deleted = 0;
    //         l++;
    //     } 
    // }
    // return max === nums.length ? max -1 : max

    // sliding window
    let l = 0;
    let k = 1;
    let max = 0;

    for(let r = 0; r < nums.length; r++) {
        if(nums[r] === 0) k -= 1;

        while(k < 0) {
            if(nums[l] === 0) k+= 1;
            l++;
        }

        max = Math.max(max, r - l)
    }
    return max;
};

