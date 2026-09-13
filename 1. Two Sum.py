# stinky poop
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for element in nums:
            nums2 = copy.copy(nums)
            nums3 = copy.copy(nums)
            nums2.remove(element)
            for element2 in nums2:
                if target - element == element2:
                    index1 = nums.index(element)
                    index2 = nums.index(element2)
                    if index1 != index2:
                        return [index1, index2]
                    else:
                        nums3[index2] = "placeholder"
                        index3 = nums3.index(element2)
                        return [index1, index3]   
                else:
                    continue

        
        
        
