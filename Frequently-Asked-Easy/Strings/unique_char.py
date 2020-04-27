s = "leetcode"

dict = {}

for i in s:
    if not i in dict:
        dict[i] = 1
    else:
        dict[i] +=1

for i,j in dict.items():
    if j==1:
        print(i)

import collections
count = collections.Counter(s)
print(count)
# find the index
for idx, ch in enumerate(s):
    if count[ch] == 1:
        print(idx)


s1 =s
while s != "":
    if s[0] not in s[1:]:
        print(s1.index(s[0])  )
    print(s,"ss")
    s = "".join(s.split(s[0]))
    print(s,"s")
