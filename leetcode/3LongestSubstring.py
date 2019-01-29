# -*- encoding:utf-8 -*-


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1

        count = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                sublen = j - i +1
                if len(set(list(s[i:j+1]))) == sublen and sublen > count:
                    count = sublen
        return count


if __name__ == "__main__":
    # 做online judge 选例是很重要的，程序员的基本功
    a = "abcabcbb"
    b = "bbbbb"
    c = "pwwkew"
    d = "au"
    e = "aab"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(a)
    print(result)
    result = solution.lengthOfLongestSubstring(b)
    print(result)
    result = solution.lengthOfLongestSubstring(c)
    print(result)
    result = solution.lengthOfLongestSubstring(e)
    print(result)
    result = solution.lengthOfLongestSubstring("")
    print(result)
    result = solution.lengthOfLongestSubstring(" ")
    print(result)
