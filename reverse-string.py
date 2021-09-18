class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len (s) -1
        if r == 0: return s
        while(r>l):
            temp = s[l]
            s[l]=s[r]
            s[r]=temp
            r-=1
            l+=1
        return s