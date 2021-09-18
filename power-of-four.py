class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        if n == 1: return True
        while (n):
            if n % 4 != 0: return False
            if n == 4: return True
            n = n / 4
        return True

