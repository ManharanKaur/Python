#Check Strict subset
A = set(map(int,input().split()))
n = int(input())
r = 0
for i in range(n):
    s = set(map(int,input().split()))
    if len(s) < len(A):
        if s.issubset(A) == True:
            r += 1
        else:
            break
    else:
        break
print(True) if r == n else print(False)
