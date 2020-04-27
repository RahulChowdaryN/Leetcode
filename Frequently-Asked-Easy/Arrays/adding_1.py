inp = ['9','9','9']

print(list(str(int("".join(inp))+1)))
s = ''
for i in inp:
    s = s+str(i)
output = int(s)+1
ins = []
for i in str(output):
    ins.append(int(i))
print(ins)
print("h")
digits = [9,9,9]
def add(digits):

    done = False
    for i in range(len(digits) - 1, -1, -1):

        if digits[i] != 9:
            digits[i] += 1
            done = True
            break
        else:
            digits[i] = 0
    if not done:
        digits.insert(0,1)
    return digits



print(add(digits))





