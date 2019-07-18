#coding=utf-8
'''
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
'''
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dictOfnum = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        #递归求解
        #退出条件 length < 1

        result = []
        lengtOfDigits = len(digits)
        print(digits[:-1])
        if lengtOfDigits < 1:
            return result

        if lengtOfDigits == 1:
            for digit in dictOfnum[digits[0]]:
                result.append(digit)
            return result
        else:
            #截取第一位到倒数第二位之前的数字
            last = digits[:-1]
            lastone = self.letterCombinations(last)
            for first in lastone:
                for second in dictOfnum[digits[-1]]:
                    result.append(first + second)
            
        return result



test=Solution()
test.letterCombinations("234")




class Solution3:
    def listCombinations(self, list_1, list_2):
        ans = []
        if len(list_1) == 0:
            return list_2
        if len(list_2) == 0:
            return list_1
        for c1 in list_1:
            for c2 in list_2:
                ans.append(c1+c2)
        return ans

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """      
        ans = []
        nums = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'} 
        for n in digits:
            list_1 = list(nums[n])
            ans = self.listCombinations(ans, list_1)
        return ans




class Solution2:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        from collections import deque
        d = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        lst=deque()
        res=[]
        l=len(digits)
        if l==0:
            return []
        for i in d[int(digits[0])]:
            lst.append(i)
        while lst:
            item=lst.popleft()
            if len(item)==l:
                res.append(item)
            else:
                for i in d[int(digits[len(item)])]:
                    lst.append(item+i)
        return res

