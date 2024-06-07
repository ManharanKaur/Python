#Designer Door Mat
s = input()
lis = s.split()
n = int(lis[0])
for i in range(1,n,2):
    x = '.|.' * i
    print(x.center(n*3,'-'))
print("WELCOME".center(n*3,'-'))
for i in range(n - 2,0,-2):
    x = '.|.' * i
    print(x.center(n*3,'-'))
