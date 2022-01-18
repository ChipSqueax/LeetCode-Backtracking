res = []
n = 3
def backtrack(comb, count):
    if len(comb) == n*2 and count == 0:
        res.append(comb)
        return
    if count < 0 or count > n or len(comb) > n*2:
        return
    backtrack(comb+"(", count+1)
    backtrack(comb+")", count-1)
backtrack("", 0)
print(res)