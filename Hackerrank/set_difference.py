# Set .difference()operation
e = int(input())
english = set(map(int,input().split()))
f = int(input())
french = set(map(int,input().split()))
print(len(english.difference(french)))
