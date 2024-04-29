/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var closeStrings = function(word1, word2) {
    if(word1.length !== word2.length) return false;

    let counts1 = {};
    word1.split('').forEach(char => {
        counts1[char] = (counts1[char] || 0) + 1;
    });

    let counts2 = {};
    word2.split('').forEach(char => {
        counts2[char] = (counts2[char] || 0) + 1;
    });

    const keys1 = Object.keys(counts1);
    const keys2 = Object.keys(counts2);
    const values1 = Object.values(counts1);
    const values2 = Object.values(counts2);

    // Sort keys and values arrays before comparison
    keys1.sort();
    keys2.sort();
    values1.sort((a, b) => a - b);
    values2.sort((a, b) => a - b);

    // Check if keys and values are the same
    return keys1.join('') === keys2.join('') && values1.join('') === values2.join('');
};

