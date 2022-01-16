s = "a1b2"
res = []
def backtrack(start, comb):
    if start == len(s):
        res.append(comb)
        return
    if not s[start].isalpha():
        backtrack(start+1, comb+s[start])
    else:
        backtrack(start+1, comb+s[start])
        backtrack(start+1, comb+s[start].swapcase())
backtrack(0, "")
print(res)