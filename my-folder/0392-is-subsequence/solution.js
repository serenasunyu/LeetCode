/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let i = 0, j = 0;
    // for(; i < s.length && j < t.length; j++) {
    //     if(s[i] === t[j]) {
    //         i++;
    //     } 
    // }

    // return i === s.length;

    while (i < s.length && j < t.length) {
        if(s[i] === t[j]) {
            i++;
        }
        j++;
    }
    return i === s.length;
};
