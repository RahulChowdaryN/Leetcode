def myAtoi( str: str) -> int:

    s = ''

    for i in str:
        if i.isspace():
            pass
        else:
            s = s+i
    if not s.startswith('-'):
        if not s[0].isdigit():
            return False

    s = ''
    for i in str:

        if i.isalpha():
            pass
        else:
            s = s+i


    if int(float(s)) <= -2147483648:

            return -2147483648

    if int(float(s)) >= 2147483649:
        return 2147483649

    return int(float(s))



print(myAtoi("-"))
