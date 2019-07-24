# -*- encoding: utf-8 -*-
'''
@File    :   Leetcode-118.py
@Time    :   2019/07/24 22:00:27
@Author  :   lpc 
@Version :   1.0
@Contact :   334193254@qq.com
@WebSite    :   
'''

# here put the import lib
'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return []
        for i in range(numRows + 1):
            if i > 0:
                result.append(self.lastList(i))
        return result

    def lastList(self,oldList: int) -> List[ int ]:   
        newList = []
        if oldList ==1:
            return [1]
        elif oldList == 2:
            return  [1,1]
        else:
            temp = self.lastList(oldList - 1)
            newList.append(1)
            for i in range(1,oldList-1) : 
                newValue = temp[i-1] + temp[i]
                newList.append(newValue)
            newList.append(1)
            return newList     

'''
方法二，直接套公式                                 
'''
test = Solution()
a = test.generate(5)
print(a)
