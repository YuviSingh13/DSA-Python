def reverseWords(s: str) -> str:
    new = s.split()
    new = new[::-1]
    s = ""
    for i in range(len(new)):
        if i == len(new)-1:
            s += new[i]
        else:
            s = s + new[i] + " "
    return s

string  = "the sky is blue"
res = reverseWords(string)
print(res)