/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    // Find the greatest common divisor length
    const gcdLength = gcd(str1.length, str2.length);
    
    // Get the potential greatest common divisor string
    const potentialGcd = str1.substring(0, gcdLength);
    
    // Check if the potential gcd divides both strings
    if (isDivisor(potentialGcd, str1) && isDivisor(potentialGcd, str2)) {
        return potentialGcd;
    } else {
        return '';
    }
    
};

// Helper function to find the greatest common divisor using Euclidean algorithm
function gcd(a, b) {
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Helper function to check if a substring divides a string
function isDivisor(substr, str) {
    const numRepeats = str.length / substr.length;
    return substr.repeat(numRepeats) === str;
}
