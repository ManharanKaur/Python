# Set  Mutations
n = int(input())
s = set(map(int,input().split()))
N = int(input())
for i in range(N):
    command = input()
    s2 = set(map(int,input().split()))
    if command.startswith("intersection") == True:
        s.intersection_update(s2)
    elif command.startswith("update") == True:
        s.update(s2)
    elif command.startswith("symmetric") == True:
        s.symmetric_difference_update(s2)
    elif command.startswith("difference") == True:
        s.difference_update(s2)
print(sum(s))
