# -*- encoding: utf-8 -*-
'''
@File    :   leetcode-832.py
@Time    :   2019/07/18 23:35:11
@Author  :   lpc 
@Version :   1.0
@Contact :   334193254@qq.com
@WebSite    :   
'''

# here put the import lib
'''
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

示例 1:

输入: [[1,1,0],[1,0,1],[0,0,0]]
输出: [[1,0,0],[0,1,0],[1,1,1]]
解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
     然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
示例 2:

输入: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
输出: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
解释: 首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
     然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
说明:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flipping-an-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import matplotlib.pyplot as plt

class Solution:

     def turnZ(self,i:int) -> int:
          if i == 0:
               return 1
          else:
               return 0



     def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        fig=plt.figure()
        ax1 = fig.add_subplot(1,2,1)
        ax2 = fig.add_subplot(1,2,2)
        ax1.matshow(A,cmap=plt.cm.gray)  
        print(A)
        
        result = []
        for i in range(len(A)) :
             A[i] = [self.turnZ(t) for t in A[i]]
             A[i].reverse()
        print(A)


        ax2.matshow(A,cmap=plt.cm.gray)
        plt.show()
        return A


test = Solution()
tA = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
strt = test.flipAndInvertImage(tA)
print(strt)

