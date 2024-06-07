# Set .discard(), .remove(), .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command = input()
    if command == "pop":
        s.pop()
    elif command.startswith("remove") == True:
        s.remove(int(command[-1]))
    elif command.startswith("discard") == True:
        s.discard(int(command[-1]))
print(sum(s))
