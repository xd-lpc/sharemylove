# -*- encoding: utf-8 -*-
'''
@File    :   Leetcode-682.py
@Time    :   2019/07/25 21:43:44
@Author  :   lpc 
@Version :   1.0
@Contact :   334193254@qq.com
@WebSite    :   
'''

# here put the import lib
'''
你现在是棒球比赛记录员。
给定一个字符串列表，每个字符串可以是以下四种类型之一：
1.整数（一轮的得分）：直接表示您在本轮中获得的积分数。
2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效 回合得分的总和。
3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效 回合得分的两倍。
4. "C"（一个操作，这不是一个回合的分数）：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。

每一轮的操作都是永久性的，可能会对前一轮和后一轮产生影响。
你需要返回你在所有回合中得分的总和。

示例 1:

输入: ["5","2","C","D","+"]
输出: 30
解释: 
第1轮：你可以得到5分。总和是：5。
第2轮：你可以得到2分。总和是：7。
操作1：第2轮的数据无效。总和是：5。
第3轮：你可以得到10分（第2轮的数据已被删除）。总数是：15。
第4轮：你可以得到5 + 10 = 15分。总数是：30。
示例 2:

输入: ["5","-2","4","C","D","9","+","+"]
输出: 27
解释: 
第1轮：你可以得到5分。总和是：5。
第2轮：你可以得到-2分。总数是：3。
第3轮：你可以得到4分。总和是：7。
操作1：第3轮的数据无效。总数是：3。
第4轮：你可以得到-4分（第三轮的数据已被删除）。总和是：-1。                                      
第5轮：你可以得到9分。总数是：8。
第6轮：你可以得到-4 + 9 = 5分。总数是13。
第7轮：你可以得到9 + 5 = 14分。总数是27。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/baseball-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:

    def calPoints(self, ops: List[str]) -> int:
        #index = 0
        everycase = []
        for v in ops:
            if v == '+':
                everycase.append(everycase[-1] + everycase[ -2])
                #index = index + 1       
            elif v == 'D':
                everycase.append(2 * everycase[-1])
                #index = index + 1    
            elif v == 'C':
                #list 中 del是按index删除元素 del list[index]  list.pop()是删除最后一个元素
                #remove的书写方式是 **list.remove(value) ** 删除第一个出现的对应元素，注意不是根据索引删除。而是确定列表种有某个元素，删除它。
                everycase.pop()
                #index = index - 1    
            else :
                everycase.append(int(v))
                #index = index + 1
        
        return sum(everycase) 

A = ["5","-2","4","C","D","9","+","+"]
test = Solution()
a = test.calPoints(A)
print(a)
