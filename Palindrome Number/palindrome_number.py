class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        b=str(x)[::-1]
        if(b==str(x)):
            return True
        else:
            return False
        