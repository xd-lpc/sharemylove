class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_num={}

        result=[0,0]
        for i in range(len(nums)) :
            if((target - nums[i]) in dict_num):
                result[0] = dict_num[target - nums[i]]
                result[1] = i
            else:
                dict_num[nums[i]] = i
            
        
        print(result)
        return result







nums = [3,2,3]
target = 6
test = Solution()
test.twoSum(nums,target)
print("2222")
