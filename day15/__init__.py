class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str 匹配项
        :type p: str 被匹配项
        :rtype: bool
        """
        flag = False
        if len(s) != len(p):
            return flag
        else:
            for i in range(len(p)):
                val = p[i]
                for i in range(len(s)):
                    if s[i] == val or val == '.':
                        flag = True
                        break
                    elif s[i] == '*':
                        if s[i - 1] == val or p[i - 1] == '.':
                            flag = True
                            break
        return flag


if __name__ == '__main__':
    s = Solution()
    s.isMatch('aab', "c*a*b")
