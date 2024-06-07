# collectionc.Counter()
import collections as cl
X = int(input())
size = list(map(int,input().split()))
N = int(input())
size_count = cl.Counter(size)
money = 0
for i in range(N):
    size_price = list(map(int,input().split()))
    if size_count[size_price[0]] != 0:
        money += size_price[1]
        size_count[size_price[0]] -= 1
print(money)
