#Find the Runner-up Score
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()[:n])
    s = set(arr)#converted to set to remove duplicates and to sort it
    l = list(s)#converted to list as set elements are not callable
    l.sort()
    print(l[-2])
