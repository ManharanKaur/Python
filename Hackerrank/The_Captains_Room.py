# The Captain's Room
n = int(input())
lis = input().split()
rooms = {}
for i in lis:
    if i in rooms:
        rooms[i] += 1
    else:
        rooms[i] = 1
for j in rooms:
    if rooms[j] == 1:
        print(j)
        break
