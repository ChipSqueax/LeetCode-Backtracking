res = []
candidates = [2,5,2,1,2]
target = 5
candidates.sort()
def backtrack(start, comb, total):
    if total == target:
        res.append(comb.copy())
        return
    if total > target or start >= len(candidates):
        return
    comb.append(candidates[start])
    backtrack(start+1, comb, total+candidates[start])
    comb.pop()
    i = start+1
    while i < len(candidates):
        if candidates[i] != candidates[i-1]:
            break
        i += 1
    backtrack(i, comb, total)
backtrack(0, [], 0)
print(res)