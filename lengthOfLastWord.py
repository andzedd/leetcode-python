class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s.isspace()):
            return 0
        res = s.split()
        return len(res[-1])