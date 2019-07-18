#coding=utf-8
'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #一句话搞定，转换成字符串
        #str(x)==str(x)[::-1]

        if x < 0:
            return False
        
        input = str(x)
        after = input[::-1]
        print (x,after)
        for i in range(len(after)):
            if after[i] != input[i]:
                return False
        
        return True






test = Solution()
x = 121
test.isPalindrome(x)
print (test.isPalindrome(x))