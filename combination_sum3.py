res = []
n = 7
k = 2
def backtrack(start, comb, total):
    if total == n and len(comb) == k:
        res.append(comb.copy())
        return
    if total > n or len(comb) > k or start > 9:
        return
    comb.append(start)
    backtrack(start+1, comb, total+start)
    comb.pop()
    backtrack(start+1, comb, total)
backtrack(1, [], 0)
print(res)