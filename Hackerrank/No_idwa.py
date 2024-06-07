# No Idea!
integers = list(map(int,input().split()))
n = list(map(int,input().split()))
mA = set(map(int,input().split()))
mB = set(map(int,input().split()))
happiness = 0
for i in n:
    if i in mA:
        happiness += 1
    elif i in mB:
        happiness -= 1
print(happiness)
