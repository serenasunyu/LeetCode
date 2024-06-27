/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {

    /*
    let stack = [];

    for (let char of s) {
        if(char === '(' || char === '[' || char === '{') {
            stack.push(char);
        } else {
            if (!stack.length || 
                (char === ')' && stack[stack.length - 1] !== '(') ||
                (char === ']' && stack[stack.length - 1] !== '[') || 
                (char === '}' && stack[stack.length - 1] !== '{')) {
                    return false;
                }
            stack.pop();
        }
    }

    return !stack.length;
    */

    const matchingBrackets = {
        ')':'(',
        ']':'[',
        '}':'{'
    };

    let stack = [];

    for (let c of s) {
        if (c in matchingBrackets) {
            const topElement = stack.length ? stack.pop() : '#';

            if (matchingBrackets[c] !== topElement) {
                return false;
            }
        } else {
            stack.push(c);
        }
    }
    
    return stack.length === 0;
};
