res = []
nums = [1,1,2]
nums.sort()
def backtrack(comb, rest):
    if len(rest) == 0:
        res.append(comb.copy())
        return 
    for i in range(len(rest)):
        if i == 0 or rest[i] != rest[i-1]:
            comb.append(rest[i])
            backtrack(comb, rest[:i]+rest[i+1:])
            comb.pop()
backtrack([], nums)
print(res)