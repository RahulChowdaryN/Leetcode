strs = ["flower","flow","flight"]
com = strs[0]
count = 0
s= ""
l =[]
for i in strs[0]:
   # print(i)
    s =s+i
    for j in strs[0:]:
        if j.startswith(s):
            continue
        else:
          #  print("else",s)
            pass

shortest = min(strs, key=len)
print("sf",shortest)
for i, w in enumerate(shortest):
    print(i,w)
    for j in range(len(strs)):
        if w != strs[j][i]:
            print( shortest[:i])
print(shortest)