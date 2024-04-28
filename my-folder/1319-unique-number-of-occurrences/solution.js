/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    // let freq = {};

    // for(let i = 0; i < arr.length; i++) {
    //     if(!(arr[i] in freq)) {
    //         freq[arr[i]] = 1;
    //     } else {
    //         freq[arr[i]] += 1;
    //     }
    // }

    // const valueSet = new Set();
    // for(let value of Object.values(freq)) {
    //     if(valueSet.has(value)) {
    //         return false;
    //     }
    //     valueSet.add(value);
    // }
    // return true;
    
    let freq = new Map();

    arr.forEach(num => freq.set(num, freq.get(num) + 1 || 1));

    const set = new Set(freq.values());

    return set.size === freq.size;
};
