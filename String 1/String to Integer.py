def myAtoi(s: str) -> int:
    arr = s.split()
    for i in arr:
        try:
            if int(i):
                if len(i) > 8 and int(i) < 0:
                    return -2 ** 31
                elif len(i) > 8 and int(i) > 0:
                    return (2 ** 31) - 1
                else:
                    return int(i)
        except:
            return 0


# ss = "   -42"
ss = "3.14159"
# ss = "4193 with words"
res = myAtoi(ss)
print(res)
