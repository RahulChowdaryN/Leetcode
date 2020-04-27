s = ["H","a","n","n","a","h"]

length = len(s)
for i in range(length//2):
    s[i],s[length-i-1] = s[length-i-1],s[i]

print(s)

