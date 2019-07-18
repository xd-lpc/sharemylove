# -*- encoding: utf-8 -*-
'''
@File    :   Leetcode303.py
@Time    :   2019/07/17 21:37:40
@Author  :   lpc 
@Version :   1.0
@Contact :   334193254@qq.com
@WebSite    :   
'''

'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class NumArray:

    def __init__(self, nums:List[int]):
        self.num = nums

    def sumRange(self, i: int, j: int) -> int:
        target = self.num[i:j+1]
        print(target)
        result = sum(target)
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0,5)
print(param_1)