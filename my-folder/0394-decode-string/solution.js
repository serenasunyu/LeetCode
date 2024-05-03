/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    const stack = [];
    let result = '';
    let num = '';

    for (const char of s) {
        if (char === '[') {
            stack.push({ result, num });
            result = '';
            num = '';
        } else if (char === ']') {
            const { result: prevResult, num: prevNum } = stack.pop();
            result = prevResult + result.repeat(Number(prevNum));
        } else if (!isNaN(Number(char))) {
            num += char;
        } else {
            result += char;
        }
    }

    return result;
}
