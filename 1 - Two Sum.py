# Title: Two Sum
# URL: https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
      
        hash={}
        for i in range(0,len(nums)):
            req =  target - nums[i]
            if req in hash:
                return ([hash[req],i])
            hash[nums[i]] = i
        return []
        