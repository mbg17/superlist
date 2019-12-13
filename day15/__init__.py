# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str 匹配项
#         :type p: str 被匹配项
#         :rtype: bool
#         """
#         flag = False
#         if len(s) != len(p):
#             return flag
#         else:
#             for i in range(len(p)):
#                 val = p[i]
#                 for i in range(len(s)):
#                     if s[i] == val or val == '.':
#                         flag = True
#                         break
#                     elif s[i] == '*':
#                         if s[i - 1] == val or p[i - 1] == '.':
#                             flag = True
#                             break
#         return flag
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str 匹配项
        :type p: str 被匹配项
        :rtype: bool
        """
        i = 0
        flag = False
        if len(s) != len(p):
            return flag
        else:
            for x in range(len(s)):
                if s[x] == p[i] or p[i] == '.':
                    flag = True
                    if i + 1 < len(p):
                        if p[i + 1] != '*':
                            p.replace(p[0:i], '')
                else:
                    if p[i] == '*':
                        if s[x - 1] == s[x] or s[x] == '.':
                            flag = True
                            p.replace(p[0:i], '')
                    else:
                        flag = False
            print(p)
            i = 0
        print(p)


if __name__ == '__main__':
    s = Solution()
    s.isMatch('aab', "c*a*b")
