class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        num = ''

        for char in s:
            if char == '[':
                stack.append((res, num))
                res = ''
                num = ''
            elif char == ']':
                prevRes, prevNum = stack.pop()
                res = prevRes + res * int(prevNum)
            elif char.isdigit():
                num += char
            else :
                res += char

        return res
