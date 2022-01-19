chars = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}
res = []
digits = "23"
def backtrack(start, comb):
    if len(digits) == 0:
        return
    if start == len(digits):
        res.append(comb)
        return
    cur = chars[str(digits[start])]
    for i in range(len(cur)):
        comb += cur[i]
        backtrack(start+1, comb)
        comb = comb[:-1]
backtrack(0, "")
print(res)