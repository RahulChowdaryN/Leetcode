s = "A man, a plan, a canal: Panama"

def remove_whitespace(s):
    print("hello")
    d = ''
    for i in s:
        if i.isalnum():
            d = d+i.lower()
    return d
pal = remove_whitespace(s)

new_list = list(pal)

new_str = "".join(new_list[::-1])
print(new_str)
print(pal)


r ="amanaplanacanalpanama"

for i in range(len(r)//2):
    if r[i] == r[len(r)-i-1]:
        continue
    else:
        print(False)
