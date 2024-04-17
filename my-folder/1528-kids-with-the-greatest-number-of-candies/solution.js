/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let maxCandies = Math.max(...candies);
    let res = [];
    for (let i = 0; i < candies.length; i++) {
        res.push((candies[i] + extraCandies >= maxCandies))
    }
    return res;
    
};
