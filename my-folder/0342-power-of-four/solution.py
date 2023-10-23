class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        '''
        mask = 0x55555555
        return n > 0 and (n & (n-1)) == 0 and (n & mask) == n
        '''
        if n == 1:
            return True
        if n <= 0:
            return False
        
        sqrtN = math.sqrt(n)
        log2SqurtN = math.log2(sqrtN)

        return log2SqurtN == int(log2SqurtN)
