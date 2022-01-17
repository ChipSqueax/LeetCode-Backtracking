res = []
candidates = [2,3,5]
target = 8
def backtrack(start, comb, total):
    if total == target:
        res.append(comb.copy())
        return
    elif total > target or start == len(candidates):
        return
    comb.append(candidates[start])
    backtrack(start, comb, total+candidates[start])
    comb.pop()
    backtrack(start+1, comb, total)
backtrack(0, [], 0)
print(res)