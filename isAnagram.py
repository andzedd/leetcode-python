class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s.strip()) != len(t.strip())):
            return False
        sTemp = ''.join(sorted(s)) 
        tTemp = ''.join(sorted(t))
        return sTemp == tTemp