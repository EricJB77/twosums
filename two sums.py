class Solution(object):    
    def twoSum(self, nums, target):        
        for x in range(len(nums)-1):
            #print(nums)
            for y in range(len(nums)):
                if nums[x] + nums[y] == target:
                    answer = [x,y]
                    print('[{0}]'.format(','.join(map(str, answer))))
                    exit()
        return



nums = [2,7,11,15]
target = 9

p  = Solution()
p.twoSum(nums,target)

'''
:type nums: List[int]
:type target: int
:rtype: List[int]
'''