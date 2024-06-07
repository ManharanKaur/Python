#Symmetric Difference
m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))
diff = sorted(list(M.difference(N)) + list(N.difference(M)))
for i in diff:
    print(i)
