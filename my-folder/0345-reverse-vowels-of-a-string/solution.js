/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    const vowels = ["a", "e", "i", "o", "u"];
    let i = 0;
    let j = s.length - 1;
    const sArray = s.split("");
    while (i < j) {
        if(vowels.includes(sArray[i].toLowerCase()) && vowels.includes(sArray[j].toLowerCase())) {
            temp = sArray[i];
            sArray[i] = sArray[j];
            sArray[j] = temp
            i++;
            j--;
        } else if (!vowels.includes(sArray[i].toLowerCase())) {
            i++;
        } else if (!vowels.includes(sArray[j].toLowerCase())) {
            j--;
        }
    }
    
    return sArray.join("");

};
