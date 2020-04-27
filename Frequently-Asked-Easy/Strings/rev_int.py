a = 1534236469


done = False
if a < 0:
    done = True

b = list(str(a))

print(b.reverse())

c = int("".join(b[:len(b) ]))
if done:
    c = int("".join(b[:len(b) - 1]))
    print(-c)

print(c)
class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = (-1) * (x)
        rev = 0
        while x > 0:
            s = x % 10
            rev = rev * 10 + s
            x = int(x / 10)

        if rev >= -2147483648 and rev <= 2147483649:
            if flag:
                return (-1) * rev
            else:
                return rev
        else:
            return 0


class Solution:
    def reverse(self, x: int) -> int:

        done = False
        if x < 0:
            done = True

        b = list(str(x))

        b.reverse()

        if done:
            c = -int("".join(b[:len(b) - 1]))
        else:
            c = int("".join(b[:len(b)]))

        if c >= -2147483648 and c <= 2147483649:

            return c
        else:
            return 0

x = 121
rev= 0
while x > 0:
    s = x % 10
    rev = rev * 10 + s
    x = int(x / 10)
print(rev)

