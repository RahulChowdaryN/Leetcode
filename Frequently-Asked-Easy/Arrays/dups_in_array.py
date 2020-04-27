## unsorted array

a = [-1,0,0,2,0,2,0,3,3]
c = None
for i in a:
    index = a.index(i)
    a.pop(index)
    if i in a:
        while i in a:
            a.remove(i)
    a.insert(index,i)

print(a)

##sorted array
a = [-1,0,0,2,0,2,0,3,3]
i = 0
length = len(a)
while i<length-1:
    if a[i] == a[i+1]:
        a.pop(i+1)
        length = length -1
    else:
        i = i+ 1
print(a)


def removeDuplicates(nums):
    prev_obj = None
    for i in range(len(nums)-1,-1,-1):
        if prev_obj == nums[i]:
            nums.pop(i)
        prev_obj = nums[i]
    return nums

nums1 = [0,0,1,2,3,4,5,5,5,5]
for i in range(len(nums1)-1,-1,-1):
    print(i)

print(removeDuplicates(nums1) )

nums = [0,0,1,2,3,4,5,5,5,5]

c=  int
for i in range(len(nums)-1,-1,-1):
    if  c == nums[i]:
        nums.pop(i)
    c = nums[i]
print(nums)


#class Solution:
#    def removeDuplicates(self, nums: List[int]) -> int:
#
#        i = 0
#        length = len(nums)
#        while i < length - 1:
#            if nums[i] == nums[i+1]:
#                nums.pop(i+1)
#                length = length -1
#            else:
#                i = i + 1
#
#        return len(nums)