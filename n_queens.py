res = []
diag1 = set()
diag2 = set()
board = []
n = 4
def checkValid(r, c, cols):
    if r-c in diag1:
        return False
    elif r+c in diag2:
        return False
    elif c in cols:
        return False
    return True

def solve(r, c, cols, count):
    if count == n:
        res.append(cols.copy())
        return
    for i in range(n):
        if checkValid(r, i, cols):
            cols.append(i)
            diag1.add(r-i)
            diag2.add(r+i)
            solve(r+1, i, cols, count+1)
            cols.pop()
            diag1.remove(r-i)
            diag2.remove(r+i)

solve(0, 0, [], 0)
retres = []
for r in res:
    temp = []
    for val in r:
        s = ""
        for i in range(n):
            if i == val:
                s+="Q"
            else:
                s+="."
        temp.append(s)
    retres.append(temp)

print(retres)