/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    // let vowels = 'aeiou';
    // let maxCount = 0;

    // for(let i = 0; i <= s.length - k; i++) {
    //     let subStr = s.slice(i, i + k);
    //     let count = 0;

    //     for(let char of subStr) {
    //         if(vowels.includes(char)) {
    //             count++
    //         }
    //     }

    //     maxCount = Math.max(maxCount, count);
    // }

    // return maxCount;

    let vowels = 'aeiou';
    let maxCount = 0;
    let count = 0;

    for (let i = 0; i < k; i++) {
        if(vowels.includes(s[i])) {
            count++;
        }
    }
    maxCount = count;

    for (let i = k; i < s.length; i++) {
        if(vowels.includes(s[i - k])) {
            count--;
        }

        if(vowels.includes(s[i])) {
            count++;
        }

        maxCount = Math.max(maxCount, count);
    }
    return maxCount;
};
