class Solution:
    def isValid(self, s: str) -> bool:

        """
        
        stack = []

        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == ']' and stack[-1] != '[') or \
                    (c == '}' and stack[-1] != '{'):
                    return False
                stack.pop()
        return not stack
        """
        # dictionary to hold matching pairs of brackets
        matching_brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        # stack to keep track of opening brackets 
        stack = []
        # traverse each characer in the string
        for char in s:
            if char in matching_brackets:
                # pop the top element from the stack if stack is not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                # check if the popped element matches the corresponding opening bracket
                if matching_brackets[char] != top_element:
                    return False
            else:
                # push the opening bracket onto the stack
                stack.append(char)
        # if the stack is empty, all brackets were matched correctly
        return not stack





