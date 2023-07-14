from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    common = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return common
        common += strs[0][i]
    return common


arr = ["flower","flow","flight"]
res = longestCommonPrefix(arr)
print(res)