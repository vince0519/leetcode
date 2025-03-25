class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_pointer, s_pointer = 0, 0

        while t_pointer < len(t) and s_pointer < len(s):
             if t[t_pointer] == s[s_pointer]:
                s_pointer += 1
             t_pointer += 1

        return s_pointer == len(s)