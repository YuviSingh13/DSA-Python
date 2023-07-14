def repeatedStringMatch(a: str, b: str) -> int:
    n, m = divmod(len(b), len(a))
    if m:
        n += 1
    if b in a * n:
        return n
    elif b in a * (n+1):
        return n+1
    else:
        return -1

a = "abcd"
b = "cdabcdab"
res = repeatedStringMatch(a, b)
print("Result : ", res)