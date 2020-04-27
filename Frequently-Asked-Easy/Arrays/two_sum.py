nums = [3,2,4]
target = 7
num = {}
for i in range(len(nums)-1,-1,-1):
    diff = target - nums[i]
    if diff in nums[:i]:
        print(nums.index(diff),i)








