/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    /** 
    let p = 1;
    let res = new Array(nums.length);
    let zeroCount = 0;
    for(let i = 0; i < nums.length; i++) {
        if(nums[i] !== 0) {
           p = p * nums[i] 
        } else {
            zeroCount ++;
        }  
    }

    if(zeroCount === 1) {
        for(let i = 0; i < nums.length; i++) {
            res[i] = nums[i] === 0 ? p : 0;
        }
    } else if (zeroCount > 1) {
        res.fill(0);
    } else {
        for(let i = 0; i < nums.length; i++) {
            res[i] = p / nums[i];
        }
    }

    return res;
    */

    const n = nums.length;
    let leftProducts = new Array(n).fill(1);
    let rightProducts = new Array(n).fill(1);
    let res = new Array(n);

    for(let i = 1; i < n; i++) {
        leftProducts[i] = leftProducts[i-1] * nums[i-1];
    }

    for(let i = n-2; i >= 0; i--) {
        rightProducts[i] = rightProducts[i+1] * nums[i+1];
    }

    for (let i = 0; i < n; i++) {
        res[i] = leftProducts[i] * rightProducts[i];
    }
    return res;
};
