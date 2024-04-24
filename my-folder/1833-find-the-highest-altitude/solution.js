/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    gain.unshift(0);
    for (let i= 1; i < gain.length; i++) {
        gain[i] = gain[i] + gain[i - 1];   
    }
    return Math.max(...gain); // use spread operator to spread the elements of the array as arguments to the fucntion
};
