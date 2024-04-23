/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let writeIndex = 0;
    let count = 1;

    for (let readIndex = 0; readIndex < chars.length; readIndex++) {
        if (readIndex + 1 === chars.length || chars[readIndex] !== chars[readIndex + 1]) {
            chars[writeIndex++] = chars[readIndex]; // Write current character

            if (count > 1) {
                const countStr = count.toString();
                for (let i = 0; i < countStr.length; i++) {
                    chars[writeIndex++] = countStr[i]; // Write count digits
                }
            }

            count = 1; // Reset count for next character
        } else {
            count++; // Increment count for consecutive characters
        }
    }

    return writeIndex; // Return the length of the compressed array
};

