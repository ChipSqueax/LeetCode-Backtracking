nums = [1,2,3]
res = []
def backtrack(start, comb):
    if start == len(nums):
        res.append(comb.copy())
        return
    comb.append(nums[start])
    backtrack(start+1, comb)
    comb.pop()
    backtrack(start+1, comb)
backtrack(0, [])
print(res)