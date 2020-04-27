nums1 = [1,2,2,1]

nums2 = [2,2]
res = []

#for i in nums1:
#    if i in nums2:
#        res.append(i)
#        nums2.remove(i)
#print(res)

if len(nums2) > len(nums1):
    nums1, nums2 = nums2, nums1

map_t = {}

for num in nums1:
    if num not in map_t:
        map_t[num] = 1
    else:
        map_t[num]+=1
ins = []
for j in nums2:
    if j in map_t:
        if map_t[j]>0:
            print("ins")
            ins.append(j)
print(ins)
