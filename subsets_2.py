res = []
nums = [1,2,2]
nums.sort()
def backtrack(start, comb):
    if start >= len(nums):
        res.append(comb.copy())
        return
    comb.append(nums[start])
    backtrack(start+1, comb)
    comb.pop() 
    i = start+1
    while i < len(nums):
        if nums[i] != nums[i-1]:
            break
        i += 1
    backtrack(i, comb)
backtrack(0, [])
print(res)