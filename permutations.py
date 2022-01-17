res = []
nums = [1,2,3]
def perm(comb, rest):
    if len(rest) == 0:
        res.append(comb.copy())
        return
    for i in range(len(rest)):
        comb.append(rest[i])
        perm(comb, rest[:i]+rest[i+1:])
        comb.pop()
perm([], nums)
print(res)