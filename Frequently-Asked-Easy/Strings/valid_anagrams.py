s = "anagram"

t = "nagaram"

import collections

count1 = collections.Counter(s)
count2 = collections.Counter(t)

for i,j in count1.items():
    if j != count2[i]:
        print(False)

s_list = list(s)
t_list= list(t)

print(t_list.sort(),s_list.sort())
print(t_list,s_list)

if t_list == s_list:
    print("True")