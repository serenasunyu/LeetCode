/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    // let answer1 = [];
    // let answer2 = [];
    // let answer = [];

    // nums1 = [...new Set(nums1)];
    // nums2 = [...new Set(nums2)];
    
    // for (let i = 0; i < nums1.length; i++) {
    //     if (!nums2.includes(nums1[i])) {
    //         answer1.push(nums1[i]);
    //     }
    // }
    // for (let i = 0; i < nums2.length; i++) {
    //     if (!nums1.includes(nums2[i])) {
    //         answer2.push(nums2[i]);
    //     }
    // }

    // answer.push(answer1);
    // answer.push(answer2);
    // return  answer;   

    const set1 = new Set(nums1);
    const set2 = new Set(nums2);

    const answer1 = [...set1].filter(num => !set2.has(num));
    const answer2 = [...set2].filter(num => !set1.has(num));

    return [answer1, answer2];
};
