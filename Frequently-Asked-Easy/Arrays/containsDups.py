nums = [1,1]
for i in range(len(nums)-1,-1,-1):
    print(i)
    a = nums.pop(i)
    print(i)
    if a in nums:
        print("found")