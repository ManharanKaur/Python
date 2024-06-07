#Exceptions
T = int(input())
for i in range(T):
    try:
        d = input().split()
        print(int(d[0])//int(d[1]))
    except ZeroDivisionError as z:
        print("Error Code:",z)
    except ValueError as v:
        print("Error Code:",v)
