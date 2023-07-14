def romanToInt(s: str) -> int:
    roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }
    score = 0
    for i in range(len(s)-1):
        if roman[s[i]] < roman[s[i+1]]:
            score -= roman[s[i]]
        else:
            score += roman[s[i]]
    return roman[s[-1]] + score


s = "LVIII"
res = romanToInt(s)
print(res)