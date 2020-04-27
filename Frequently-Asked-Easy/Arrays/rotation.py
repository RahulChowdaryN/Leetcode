nums = [1,2,3,4,5,6,7]

i = 3

length = len(nums)

nums = nums[length-i:] + nums[:length-i]
print(nums)

