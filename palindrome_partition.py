res = []
s = "aab"
def backtrack(start, comb):
    if start >= len(s):
        res.append(comb.copy())
        return
    for i in range(start, len(s)):
        st = s[start:i+1]
        if st == st[::-1]:
            comb.append(st)
            backtrack(i+1, comb)
            comb.pop()
backtrack(0, [])
print(res)