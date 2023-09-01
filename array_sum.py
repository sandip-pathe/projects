class Solution:
    def twoSum(self, nums:[], target: int):
        for op1 in enumerate(self.nums):
            for op2 in enumerate(self.nums):
                if op1 + op2 == target:
                    return [nums.index(op1), nums.index(op2)]
                else:
                    return "does not contain such elements"
    
    print(twoSum([2, 4, 5, 6], 6))