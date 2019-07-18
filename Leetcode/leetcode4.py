#coding=utf-8
'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

你可以假设 nums1 和 nums2 不同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newNums = []
        len1 = len(nums1)
        len2 = len(nums2)
        i = 0
        j = 0
        
        while j + i < len2 + len1:

            if i == len1 :                
                newNums.append(nums2[j])
                j = j + 1
                continue
            if j == len2 :
                newNums.append(nums1[i])
                i = i + 1
                continue

            if nums1[i] < nums2[j]:
                newNums.append(nums1[i])                
                i = i+1
            else:
                newNums.append(nums2[j])
                
                j = j + 1
        
        
        
        print (newNums)
        Median = (len2 + len1)/2
        if (len2 + len1) % 2 == 0:
            return (newNums[int(Median)] + newNums[int(Median-1)])/2
        else:
            return newNums[int(Median)]

nums1 = [1, 3,5,7,9]
nums2 = [2,3,8]
test = Solution()
test.findMedianSortedArrays(nums1,nums2)
print (test.findMedianSortedArrays(nums1,nums2))

