#coding=utf-8
'''
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 无重复字符的最长子串是 "abc"，其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 无重复字符的最长子串是 "b"，其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 无重复字符的最长子串是 "wke"，其长度为 3。
     请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。
'''
#思路：依次更新滑窗两边边界范围
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengthOfS = len(s)
        begin = 0 
        end = 0
        maxlist = []
        result = 0
        while begin < lengthOfS and end < lengthOfS:
            if s[end] not in maxlist:
                
                maxlist.append(s[end])
                end = end + 1
                result = max(result,(end - begin))
                
            else:
                begin = begin + 1
                maxlist.pop(0)
            print ("begin : ",begin,"end : ",end )
            print (maxlist)

        return result

#思路：只更新滑窗左边界
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengthOfS = len(s)
        
        stringIndex = {}
        left = 0
        maxSubString = 0
        for i in range(lengthOfS):
            if s[i] in stringIndex:
                #如果当前字符在之前已经出现过，更新左边界
                left = max(left,stringIndex[s[i]]+1)
                
            maxSubString =max (i - left + 1,maxSubString)
            stringIndex[s[i]] = i 
        return maxSubString


    
S = "abcaaefg"
test = Solution()
print (test.lengthOfLongestSubstring2(S))