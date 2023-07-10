# Given a row number r and column number c. Print the element at position (r, c) in pascal's triangle
def nCr(n, r):
    res = 1
    for i in range(r):
        res = res*(n-i)
        res = res / (i+1)
    return res

z = nCr(5, 3)

# Given a row number n. Print the n-th row of pascal's triangle

# Approach 1 (Naive Approach)
n = 4
s = ""
for i in range(n+1):
    res = nCr(n, i)
    s = s + str(int(res)) + ' '
print("N-th row of Pascal's Triangle is : ", s)

# Approach 2 (Optimal Approach)
ans = 1
print(ans, end=' ')
for i in range(1, n):
    ans = ans*(n-i)
    ans = ans/i
    print(int(ans), end=' ')
print()


# Given the number of rows n. Print the first n rows of Pascal's Triangle

# Approach 1 (Optimal Approach)
l = []
for j in range(1, n+1):
    temp = []
    ans = 1
    temp.append(ans)
    for i in range(1, j):
        ans = ans*(j-i)
        ans = ans/i
        temp.append(int(ans))
    l.append(temp)
print("Pascal's triangle : ", l )

# Approach 2 (Optimal Approach)

