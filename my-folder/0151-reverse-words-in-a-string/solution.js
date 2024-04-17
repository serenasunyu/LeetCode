/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let words = s.split(" ").filter(word => word !== "");

    for (let i = 0; i < (words.length/2); i++) {
        let temp = words[i];
        words[i] = words[words.length-1-i];
        words[words.length-1-i] = temp;
    }

    return words.join(" ");
};
