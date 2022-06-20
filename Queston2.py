class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        n = len(nums)
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        result.append([nums[i],nums[j],nums[k]])
        return result
Num=py_solution()
print(Num.threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
